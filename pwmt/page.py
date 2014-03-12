from pwmt import app
import io
import os
import yaml
import itertools
import werkzeug

class Page(object):

    def __init__(self, filePath, endpoint):
        try:
            with io.open(filePath, encoding='utf8') as fd:
                self.head = ''.join(itertools.takewhile(unicode.strip, fd))
                self.body = fd.read()

            self.meta = yaml.safe_load(self.head) or {}
            self.type = "page"
            self.filePath = filePath
            self.page_url = "#"
        except:
            raise ValueError("File '%s' does not exist", filePath)

    def path(self):
        return self.filePath

    def url(self):
        return self.page_url

    @werkzeug.cached_property
    def html(self):
        return self.body

    def tags(self):
            if 'tags' in self.meta:
                return self.meta['tags'].split(", ")
            else:
                return []

    def __getitem__(self, name):
        if name in self.meta:
            return self.meta[name]
        return None


class PageManager(object):

    suffix = ".md"

    def __init__(self, dirPath):
        self.root = dirPath

    @werkzeug.cached_property
    def _pages(self):
        pages = {}

        for root, subFolders, files in os.walk(self.root):
            for fileName in files:
                filePath = os.path.join(root, fileName)
                if filePath.endswith(self.suffix):
                    urlPath = filePath[len(self.root):-len(self.suffix)]
                    pages[urlPath] = Page(filePath, urlPath)

        return pages

    def clear(self):
        try:
            del self.__dict__['_pages']
        except KeyError:
            pass

    def get(self, path, default=None):
        pages = self._pages
        try:
            return pages[path]
        except KeyError:
            return default

    def getAll(self):
        return self._pages
