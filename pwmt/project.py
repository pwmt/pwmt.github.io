import os
import io
import json
from pwmt.page import PageManager
from pwmt.menu import Menu, MenuItem
from pwmt.news import NewsItem


def calculate_sha2_of_file(filepath):
    import hashlib
    with open(filepath, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


class Version():

    def __init__(self, project, meta):
        self.project = project

        self.name = meta["name"]
        self.date = meta["date"]
        self.changelog = meta["changelog"] if "changelog" in meta else {}

        try:
            self.filename = "%s-%s.tar.gz" % (project.name, self.name)
            self.path = os.path.join(project.path, "download", self.filename)
            self.sha2 = calculate_sha2_of_file(self.path)
        except:
            print "Can not read file for version '%s-%s'" % (self.project.name, self.name)
            pass

    def getNewsItem(self):
        news = NewsItem()
        news["title"] = "%s %s" % (self.project.name, self.name)
        news["date"] = self.date
        news["tags"] = ["release"]
        news["categories"] = [self.project.name]

        if len(self.changelog) > 0:
            content = "<h2>Changelog</h2><ul>"
            for change in self.changelog:
                content += "<li>%s</li>" % change
            content += "</ul>"
            content += "<h2>Download</h2>"
            content += "<p>You can download the latest version "
            content += "<a href='/projects/" + \
                self.project.name + "/download'>"
            content += "here.</a></p>"
            news.body += content

        return news


class Project():

    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.description = ""
        self.versions = []
        self.pageManager = PageManager(path)

        tmp_versions = {}
        info_file = os.path.join(path, "info.json")
        try:
            with io.open(info_file, encoding='utf8') as fd:
                try:
                    self.json = json.load(fd)
                    self.name = self.json["name"]
                    self.description = self.json["description"]
                    if "versions" in self.json:
                        tmp_versions = self.json["versions"]
                    self.options = self.json[
                        "options"] if "options" in self.json else {}

                    if "plugin" in self.options and self.options["plugin"] == True:
                        self.plugin = True
                    else:
                        self.plugin = False
                except NameError:
                    raise ValueError("Could not parse project: '%s'", name)
        except Exception:
            raise ValueError("Could not open project info file: '%s'", name)

        for tmp_version in tmp_versions:
            try:
                self.versions.append(Version(project=self, meta=tmp_version))
            except Exception:
                print "Could not parse version information: %s" % tmp_version

    def __exit__(self, type, value, traceback):
        pass

    def getPage(self, page):
        return self.pageManager.get(page)

    def getMenu(self):
        pages = self.pageManager.getAll()
        keylist = pages.keys()
        keylist.sort()
        menu = Menu(html_class="nav navbar-nav")
        menu.addItem(MenuItem('Home', "/projects/" + self.name))

        if self.versions and len(self.versions) > 0:
            menu.addItem(MenuItem('Download', "/projects/" + self.name +
                                  "/download/"))

        for key in keylist:
            if 'index' in key:
                continue
            menuItem = MenuItem(
                pages[key]['title'],
                "/projects/" + self.name + key)
            menu.addItem(menuItem)

        return menu


class ProjectManager():

    def __init__(self, app=None):
        self.projects = []
        self.root = os.path.join(
            app.root_path, "..", app.config['PROJECTS_PATH'])
        self.reload()

    def reload(self):
        self.projects = []
        files = os.listdir(self.root)
        files.sort()

        for file in files:
            path = os.path.join(self.root, file)
            if os.path.isdir(path):
                try:
                    project = Project(file, path)
                    self.projects.append(project)
                except:
                    pass

    def getAll(self):
        return self.projects

    def getByName(self, name):
        for project in self.projects:
            if project.name == name:
                return project
        return None
