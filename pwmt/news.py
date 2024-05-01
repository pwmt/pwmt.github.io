import yaml
import itertools
import io
import re
from unidecode import unidecode
from flask import url_for
import werkzeug
import os
import codecs


_punct_re = re.compile(r'\W+')


def slugify(text, delim='-'):
    result = []
    for word in _punct_re.split(text.lower()):
        result.extend(unidecode(word).split())
    return delim.join(result)


class NewsItem():

    def __init__(self, filepath=None):
        self.path = filepath
        self.meta = {}
        self.body = ""

        if filepath is not None:
            self.__parse_file(filepath)

        if "tags" not in self.meta:
            self.meta["tags"] = []
        if "categories" not in self.meta:
            self.meta["categories"] = []

    def __parse_file(self, filepath):
        with codecs.open(filepath, 'r', 'utf8') as fd:
            content = fd.readlines()

            head = ""
            for idx, line in enumerate(content):
                if line == "\n":
                    break

                head += line

            self.body = " ".join([x.strip() for x in content[idx:]]).strip()
            self.meta = yaml.safe_load(head) or {}

            self.meta['tags'] = self.meta['tags'].split(
                ", ") if 'tags' in self.meta else []
            self.meta['categories'] = self.meta['categories'].split(
                ", ") if 'categories' in self.meta else []

    @property
    def date(self):
        if 'date' in self.meta:
            return self.meta['date']
        else:
            return "1970-01-01"

    @property
    def url(self):
        return "/news/" + self.slug

    @property
    def slug(self):
        if 'title' in self.meta:
            return slugify(self.meta['title'])
        else:
            raise ValueError("News item has no title: '%s'" % self.path)

    def __getitem__(self, key):
        if key in self.meta:
            return self.meta[key]
        return "Unknown property: '" + key + "'"

    def __setitem__(self, key, value):
        self.meta[key] = value


class NewsManager():

    suffix = ".md"
    posts = []

    def __init__(self):
        pass

    def read_directory(self, dirpath):
        try:
            for root, subFolders, files in os.walk(dirpath):
                for filename in files:
                    filepath = os.path.join(root, filename)
                    if filepath.endswith(self.suffix):
                        self.posts.append(NewsItem(filepath=filepath))
        except:
            raise ValueError("Could not read '%s'" % dirpath)

    def add_item(self, item):
        if isinstance(item, NewsItem):
            self.posts.append(item)
        else:
            raise ValueError("The passed item must be a NewsItem")

    def remove_item(self, item):
        self.posts.remove(item)

    def clear(self):
        self.posts = []

    def getAllByDate(self):
        self.posts.sort(key=lambda x: x.meta["date"], reverse=True)
        return self.posts

    def getByTag(self, tag):
        tagged = [
            post for post in self.posts if tag in post.meta.get('tags', [])]
        tagged.sort(key=lambda x: x.meta["date"], reverse=True)
        return tagged

    def getByCategory(self, category):
        filtered = [
            post for post in self.posts if category in post.meta.get('categories', [])]
        filtered.sort(key=lambda x: x.meta["date"], reverse=True)
        return filtered

    def getBySlug(self, slug):
        for post in self.posts:
            if post.slug == slug:
                return post
        return None

    def getAllTags(self):
        tags = []
        for post in self.posts:
            for tag in post["tags"]:
                if tag not in tags:
                    tags.append(tag)

        return tags

    def getAllCategories(self):
        categories = []
        for post in self.posts:
            for category in post["categories"]:
                if category not in categories:
                    categories.append(category)

        return categories
