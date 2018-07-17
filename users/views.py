from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    # return HttpResponse("hello django")
    return render(request,"index.html")

def news(request,category,page):
    return HttpResponse("显示新闻:%s %s"%(category,page))