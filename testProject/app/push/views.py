#!coding:utf-8
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from config import settings
import os
import time

from .models import myfile,myfile_obj


def base(request):
    return render(request,'push/push_base.html')
    # return HttpResponse("ok")

def ajax_base_file(request):
    if request.method == 'POST':
        # 获取文件
        file = request.FILES.get('file')
        if not file:
            return HttpResponse("文件传输失败")

        # 文件名
        # filedir =os.path.join(settings.BASE_DIR,'image')
        # 判断目录是否存在

        filedir =os.path.join(settings.BASE_DIR,'image',time.strftime("%Y"),time.strftime("%m"),time.strftime("%d"))

        if not os.path.exists(filedir):
            # 创建目录
            os.makedirs(filedir)

        # 文件
        imagedir = os.path.join(filedir,file.name)

        # 内存写入文件
        try:
            with open(imagedir, 'wb+') as destination:
                for chunk in file.chunks(chunk_size=5242880):
                    destination.write(chunk)
        except Exception():
            return HttpResponse("保存失败")
        else:
            return JsonResponse({"text":"上传成功",'name':filedir,'size':file.size})

def ajax_base_model(request):
    if request.method == 'POST':
    # 获取文件
        file = request.FILES.get('file')
        if not file:
            return HttpResponse("文件传输失败")

        # f = myfile(name=file.name,pic=file)
        # f.save()

        # 自定义存储
        # f=myfile_obj().create(name = file.name, pic=file)
        # 存储缩略图
        f=myfile_obj().thumbSave(name=file.name,pic=file)
        return HttpResponse("保存成功")



        # return HttpResponse("保存成功:%s:%s:%s" % (f.pic.path.encode('utf-8'),
                                                   # f.pic.name.encode('utf-8'),
                                                   # f.pic.url.encode('utf-8')
            # ))

def ajax_find(request):
    if not request.method=='POST':
        return HttpResponse("非post")

    id_ = request.POST.get("id")
    id_=int(id_)

    # 使用模型模块中的方法

    t = myfile_obj().get(id=id_)
    # s=t.getfield("name")
    s = t.getPicName()

    return JsonResponse({"id":s})







if __name__=='__main__':
    pass

