from pwmt import app
import io
import os
import yaml
import itertools
from werkzeug.utils import cached_property
from pathlib import Path

class Page(object):

    def __init__(self, filePath, endpoint):
        filePath = Path(filePath).resolve()
        try:
            with open(filePath) as fd:
                content = fd.readlines()

                head = ""
                for idx, line in enumerate(content):
                    if line == "\n":
                        break

                    head += line

                self.body = " ".join(content[idx:]).strip()
                self.head = head

            self.meta = yaml.safe_load(self.head) or {}
            self.type = "page"
            self.filePath = Path(filePath).resolve()
            self.page_url = "#"
            self.endpoint = endpoint
        except:
            raise ValueError("File '%s' does not exist" % filePath)

    def path(self):
        return self.filePath

    def url(self):
        return self.page_url

    @cached_property
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

    @cached_property
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
