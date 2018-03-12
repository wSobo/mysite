#!/usr/bin/python3
"""
    ----coding:utf-8----
    @Author   : sobo
    @Time     : 2018/3/9 上午11:16
    @Software : 
    @File     : forms.py

"""
from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
