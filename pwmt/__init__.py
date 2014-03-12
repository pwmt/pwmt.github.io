from flask import Flask
from flaskext.markdown import Markdown
from flaskext.sass import sass
import os

# read configuration
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')

# setup sass css
sass(app, input_dir='assets/scss', output_dir='css')

# setup markdown
Markdown(app, extensions=['codehilite', 'extra', 'toc'])

# project manager
from pwmt.project import ProjectManager
project_manager = ProjectManager(app)

# news
from pwmt.news import NewsManager
news_dir = os.path.join(app.root_path, "..", app.config['NEWS_PATH'])
news_manager = NewsManager()
news_manager.read_directory(news_dir)

app.jinja_env.globals['projects'] = project_manager.getAll()

# page manager
from pwmt.page import PageManager
root = os.path.join(app.root_path, "..", app.config['PAGE_PATH'])
page_manager = PageManager(root)

# setup main menu
from pwmt.menu import Menu, MenuItem

menu = Menu(html_class="nav navbar-nav navbar-right")

menu.addItem(MenuItem("About Us", "/about"))
menu.addItem(MenuItem("News", "/news"))

menuItem = MenuItem("Projects", "/projects")

for project in project_manager.getAll():
    if project.options and "show_index" in project.options and project.options["show_index"] == False:
        continue
    else:
        menuItem.addSubItem(
            MenuItem(project.name, "/projects/" + project.name))
menu.addItem(menuItem)

menuItem = MenuItem("Help", "/help")
menuItem.addSubItem(MenuItem("Bug tracker", "http://bugs.pwmt.org"))
menuItem.addSubItem(MenuItem("Localization", "/help/localization/"))
menuItem.addSubItem(MenuItem("Donate", "/help/donate/"))
menuItem.addSubItem(MenuItem("Coding standard", "/help/coding-standard/"))
menu.addItem(menuItem)

menu.addItem(MenuItem("Community & Contact", "/contact"))

app.jinja_env.globals['main_menu'] = menu


def import_news_from_project_versions():
    for project in project_manager.getAll():
        for version in project.versions:
            news_manager.add_item(version.getNewsItem())

import_news_from_project_versions()


def conditional_auto_reset():
    page_manager.clear()
    news_manager.clear()
    news_manager.read_directory(news_dir)
    import_news_from_project_versions()
    project_manager.reload()

if app.config['DEBUG']:
    app.before_request(conditional_auto_reset)

# import views
import pwmt.views
