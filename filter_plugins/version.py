#!/usr/bin/env python

from packaging import version
from requests import get

class FilterModule(object):

    def filters(self):
        return {
            "kube_latest": self.kube_latest,
            "kube_is_latest": self.kube_is_latest,
            "gh_latest": self.gh_latest,
            "gh_is_latest": self.gh_is_latest,
        }

    def gh_is_latest(self, ver, repo):
        return version.parse(self.gh_latest(repo)) <= version.parse(ver)

    def gh_latest(self, repo):
        url = "https://api.github.com/repos/{0}/releases/latest".format(repo)
        return self.gh_get_version(url)

    def gh_get_version(self, url):
        res = get(url)
        tag = res.json()["tag_name"]
        return tag.replace("v", "")

    def kube_is_latest(self, ver, label):
        return version.parse(self.kube_latest(label)) <= version.parse(ver)

    def kube_latest(self, label):
        url = "https://storage.googleapis.com/kubernetes-release/release/{0}.txt".format(label)
        return self.kube_get_version(url)

    def kube_get_version(self, url):
        res = get(url)
        return res.text.replace("v", "")
