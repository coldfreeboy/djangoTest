#!coding:utf-8
from django.conf.urls import url,include
from . import views


urlpatterns = [
    # 一个模块或者插件或者测试用一个url

    # 图片和文件上传
    url(r'^base/$',views.base),
    url(r'^ajax_base_file/$',views.ajax_base_file),
    url(r'^ajax_base_model/$',views.ajax_base_model),
    url(r'^ajax_find/$',views.ajax_find),
    url(r'^ajax_uploadify/$',views.ajax_uploadify),

]
