#!/usr/bin/python3
"""
    ----coding:utf-8----
    @Author   : sobo
    @Time     : 2018/3/15 上午11:13
    @Software : 
    @File     : sitemaps.py

"""

from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.publish
