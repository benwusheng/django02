from django.http.response import HttpResponse


def check_ip(view_fun):
    def wrapper(self,request,*args,**kwargs):
        ip=request.META.get("REMOTE_ADDR")
        if ip in ["127.0.0.1"]:
            return HttpResponse("禁止ip访问")
        return view_fun(self,request,*args,**kwargs)
    return wrapper