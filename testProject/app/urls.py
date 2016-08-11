#!/usr/bin/env python  
#!coding:utf-8

from django.conf.urls import url,include
from .push import urls


urlpatterns = [
    # 一个模块或者插件或者测试用一个url

    # 图片和文件上传
    url(r'^push/',include(urls)),

]
