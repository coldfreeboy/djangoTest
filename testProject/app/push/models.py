#!coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.core.files.storage import FileSystemStorage
from config import settings
import os
from config import settings
from PIL import Image
from io import BytesIO
import time

# 设置存储路径

url_base = settings.BASE_DIR
file_url = os.path.join(url_base,"image")


fs = FileSystemStorage(location=file_url)

# Create your models here.
class myfile(models.Model):
    name = models.CharField(max_length=30)
    pic = models.ImageField(upload_to="push/%Y/%m/%d",storage=fs)



class myfile_obj():
    def __init__(self):
        # 把数据库初始化
        self._obj = myfile.objects
        self._qlist = ""

    def get(self,**kwg):
        self._qlist=self._obj.get(**kwg)
        return self

    def getUrl(self):
        return self._qlist.pic.url

    def create(self,**kwag):
        try:
            t = self._obj.create(**kwag)
        except Exception():
            return("创建失败:%s" % t)
        else:
            self._qlist=t
            return t

    def getUrlById(self,id):
        return self._obj.get(id=id).pic.url

    def getfield(self,field):
        return getattr(self._qlist,field)

    def getPicName(self):
        return self._qlist.pic.name

    def thumbSave(self,**kwg):
        # 保存成缩略图
        imgs = kwg.pop('pic')
        # 缩略图制作
        img = Image.open(imgs)

        img.thumbnail((150,150),Image.ANTIALIAS) 

        # 构造时间路径
        subPath = os.path.join(time.strftime("%Y"),time.strftime("%m"),time.strftime("%d"))

        # 构造保存地址
        filedir =os.path.join(settings.BASE_DIR,'image',subPath)

        if not os.path.exists(filedir):
            # 创建目录
            os.makedirs(filedir)


        # 文件保存地址
        imagedir = os.path.join(filedir,imgs.name)
        img.save(imagedir,'jpeg')

        # url地址
        imgUrl = os.path.join('/media',subPath,imgs.name)
        
        return imgUrl





    

        


