

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def index(request):
    # return HttpResponse("hello django")
    return render(request,"index.html")

def news(request,category,page):
    return HttpResponse("显示新闻:%s %s"%(category,page))

def news2(request):
    categorg=request.GET.get("category")
    page_no=request.GET.get("page_no")

    text="news2:%s %s"%(categorg,page_no)

    return HttpResponse(text)

def news3(request):
    category=request.POST.get("category")
    page=request.POST.get("page")

    text='获取body中的键值对:<br/>　category=%s, page=%s' % (category, page)

    return HttpResponse(text)

def news4(request):

    host=request.META.get("HTTP_HOST")
    port=request.META.get("HTTP_PORT")
    # print(request.META.get("HTTP_HOST"),request.META.get("HTTP_PORT"))
    return HttpResponse(host)

def resp(request):
    # return redirect("/index")
    # return HttpResponseRedirect("/index")
    # url=reverse("index")

    url=reverse('users:index')
    print(url)
    return redirect(url)


def set_cookie(request):
    response=HttpResponse("保存cookie数据成功")
    response.set_cookie('user_id',10)
    response.set_cookie("user_name","admin")
    return response

def get_cookie(request):
    user_id=request.COOKIES.get("user_id")
    user_name=request.COOKIES.get("user_name")
    text="user_id=%s,user_name=%s"%(user_id,user_name)

    return HttpResponse(text)


def set_session(request):
    request.session["user_id"]=100
    request.session["user_name"]='python'

    return HttpResponse("保存session成功")

def get_session(request):
    user_id=request.session.get("user_id")
    user_name=request.session.get("user_name")

    return HttpResponse((user_id,user_name))

def del_session(request):

    request.session.flush()

    return HttpResponse("session已经清空")

def post(request):
    return render(request,"post.html")

def do_post(request):
    title=request.POST.get("title")
    content=request.POST.get('content')

    text="发帖成功:title=%s,content=%s"%(title,content)
    return HttpResponse(text)