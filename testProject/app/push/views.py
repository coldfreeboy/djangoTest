#!coding:utf-8
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from config import settings
import os
import time


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


if __name__=='__main__':
    pass

