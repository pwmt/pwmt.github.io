from pwmt import app, project_manager, news_manager, page_manager, freezer
from flask import render_template, send_file, abort, request, url_for
from flask_paginate import Pagination
from pygments.formatters import HtmlFormatter as PygmentsHtmlFormatter
from urllib.parse import urljoin
from feedgen.feed import FeedGenerator
from datetime import datetime
from pathlib import Path
import os
import pytz


def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)

app.jinja_env.globals['url_for_other_page'] = url_for_other_page


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about/')
def about():
    page = page_manager.get("about")
    if page is None:
        abort(404)
    return render_template('about.html', page=page)


@app.route('/contact/')
def contact():
    page = page_manager.get("contact")
    if page is None:
        abort(404)
    return render_template('contact.html', page=page)


@app.route('/help/')
def help():
    page = page_manager.get("help")
    if page is None:
        abort(404)
    return render_template('help.html', page=page)


@app.route('/news/', defaults={'page': 1})
@app.route('/news/page/<int:page>/')
def posts(page):
    tags = news_manager.getAllTags()
    categories = news_manager.getAllCategories()
    per_page = int(app.config['POSTS_PER_PAGE'])
    start = per_page * (page - 1)
    posts = news_manager.getAllByDate()
    count = len(posts)
    posts = posts[start:(start + per_page)]

    pagination = Pagination(page=page,
                            total=count,
                            search=False,
                            per_page=per_page,
                            bs_version=3)

    return render_template(
        'posts.html',
        posts=posts,
        tags=tags,
        categories=categories,
        pagination=pagination)


@freezer.register_generator
def posts():
    posts = news_manager.getAllByDate()
    per_page = int(app.config['POSTS_PER_PAGE'])
    count = len(posts)

    yield {}

    for p in range(1, int(count / per_page)):
        yield {'page': p}


@app.route('/news/<path:slug>/')
def post(slug):
    post = news_manager.getBySlug(slug) or abort(404)
    return render_template('post.html', post=post)


@freezer.register_generator
def post():
    for item in news_manager.posts:
        yield {'slug': item.slug}


def render_posts(posts, page):
    if len(posts) == 0:
        abort(404)
    else:
        per_page = int(app.config['POSTS_PER_PAGE'])
        start = per_page * (page - 1)
        count = len(posts)
        posts = posts[start:(start + per_page)]
        tags = news_manager.getAllTags()
        categories = news_manager.getAllCategories()

        pagination = Pagination(page=page,
                                total=count,
                                search=False,
                                per_page=per_page,
                                bs_version=3)

        return render_template(
            'posts.html',
            posts=posts,
            tags=tags,
            categories=categories,
            pagination=pagination)


@app.route('/news/tag/<string:tag>/', defaults={'page': 1})
@app.route('/news/tag/<string:tag>/page/<int:page>/')
def tags(tag, page):
    posts = news_manager.getByTag(tag)
    return render_posts(posts, page)

@app.route('/news/category/<string:category>/', defaults={'page': 1})
@app.route('/news/category/<string:category>/page/<int:page>/')
def category(category, page):
    posts = news_manager.getByCategory(category)
    return render_posts(posts, page)


@app.route('/projects/<project_name>/download/')
@app.route('/projects/<project_name>/download/<path>')
def project_download(project_name, path=None):
    project = project_manager.getByName(project_name)
    if project:
        if path:
            try:
                path = '../projects/' + project_name + "/download/" + path
                return send_file(path)
            except:
                abort(404)
        else:
            return render_template('project-download.html', project=project)
    else:
        abort(404)


@freezer.register_generator
def project_download():
    projects = project_manager.getAll()
    for project in projects:
        yield {'project_name': project.name}

        path = '../projects/' + project.name + "/download/"
        pathlist = Path(path).glob('**')
        for path in pathlist:
            yield {'project_name': project.name, 'path': path}


@app.route('/projects/<project_name>/changelog/')
@app.route('/projects/<project_name>/changelog/<path:version_number>/')
def project_changelog(project_name, version_number=None):
    project = project_manager.getByName(project_name)
    if project:
        version = None
        for ver in project.versions:
            if ver.name == str(version_number):
                version = ver
                break
        if version_number is not None and version is None:
            return abort(404)
        return render_template(
            'project-changelog.html',
            project=project,
            version=version)
    return abort(404)


@freezer.register_generator
def project_changelog():
    projects = project_manager.getAll()
    for project in projects:
        for ver in project.versions:
            yield {'project_name': project.name, 'version_number': ver.name}


@app.route('/projects/<project_name>/doxygen/')
@app.route('/projects/<project_name>/doxygen/<path:filename>')
def project_doxygen(project_name, filename="index.html"):
    project = project_manager.getByName(project_name)
    if project:
        try:
            return send_file(os.path.join(project.path, "doxygen", filename))
        except:
            return abort(404)
    return abort(404)


@freezer.register_generator
def project_doxygen():
    projects = project_manager.getAll()
    for project in projects:
        doxygen_path = os.path.join(project.path, "doxygen")
        pathlist = Path(doxygen_path).glob('**')
        for path in pathlist:
            yield {'project': project.name, 'path': path}


@app.route('/projects/<project_name>/')
@app.route('/projects/<project_name>/<path:path>/')
def project(project_name, path="index"):
    project = project_manager.getByName(project_name)
    if project:
        page = project.getPage("/" + path)
        is_index = True if (path == "index") else False
        if page:
            if project.plugin:
                return render_template(
                    'project-plugin.html',
                    project=project,
                    page=page,
                    is_index=is_index)
            else:
                return render_template(
                    'project.html',
                    project=project,
                    page=page,
                    is_index=is_index)
        else:
            try:
                path = '../projects/' + project_name + "/" + path
                return send_file(path)
            except:
                abort(404)
    else:
        abort(404)

@freezer.register_generator
def project():
    projects = project_manager.getAll()
    for project in projects:
        yield {'project_name': project.name}

        for path in project.pageManager._pages.keys():
            yield {'project_name': project.name, 'path': path}


@app.route('/<path:path>/')
def page(path):
    page = page_manager.get(path)
    if page:
        return render_template('page.html', page=page)
    else:
        try:
            path = 'pages/' + path
            return send_file(path)
        except:
            abort(404)


@freezer.register_generator
def page():
    for page in page_manager._pages.keys():
        yield {'path': page}


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.route('/static/css/pygments.css')
def pygments_css():
    formatter = PygmentsHtmlFormatter(style='pastie')
    return formatter.get_style_defs(
        '.codehilite'), 200, {'Content-Type': 'text/css'}


def make_external(url):
    return urljoin(request.url_root, url)


def recent_feed():
    feed = FeedGenerator()

    feed.id(request.url_root)
    feed.title('pwmt.org')
    feed.description('Recent Articles')
    feed.link(href='https://pwmt.org')

    posts = news_manager.getAllByDate()

    timezone = pytz.timezone('Europe/Vienna')

    for post in posts:
        fe = feed.add_entry()
        fe.link(href=make_external(post.slug), rel='alternate')

        date = datetime.strptime(post.date, "%Y/%m/%d")
        date = timezone.localize(date)

        fe.title(post['title'])
        fe.content(post.body, type='html')
        fe.id(make_external(post.slug))
        fe.author({'name': "pwmt.org"})
        fe.updated(date)
        fe.published(date)

    return feed

@app.route('/atom.xml')
def atom_feed():
    feed = recent_feed()
    return feed.atom_str(pretty=True)

@app.route('/news.xml')
def rss_feed():
    feed = recent_feed()
    return feed.rss_str(pretty=True)
