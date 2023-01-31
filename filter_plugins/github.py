#!/usr/bin/env python

from packaging import version
from requests import get

class FilterModule(object):

    def filters(self):
        return {
            'is_latest': self.is_latest,
            'latest': self.latest,
        }

    def is_latest(self, ver, repo):
        return version.parse(self.latest(repo)) <= version.parse(ver)

    def latest(self, repo):
        url = "https://api.github.com/repos/{0}/releases/latest".format(repo)
        res = get(url)
        tag = res.json()["tag_name"]
        return tag.replace("v", "")
