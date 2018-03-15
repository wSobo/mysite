#!/usr/bin/python3
"""
    ----coding:utf-8----
    @Author   : sobo
    @Time     : 2018/3/15 下午3:04
    @Software : 
    @File     : feeds.py

"""

from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post


class LatestPostsFeed(Feed):
    title = 'My blog'
    link = '/blog/'
    description = 'New posts of my blog.'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)
