from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

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