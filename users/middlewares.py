from django.utils.deprecation import MiddlewareMixin


class MyMiddleware(MiddlewareMixin):
    def __init__(self,get_response=None):
        super().__init__(get_response)
        print("init")

    def process_request(self,request):
        print("before 视图")

    def process_response(self,request,response):
        print("after 视图")
        return response


class MyMiddleware2(MiddlewareMixin):
    def __init__(self, get_response=None):
        super().__init__(get_response)
        print("init")

    def process_request(self,request):
        print("before 视图 2")

    def process_response(self,request,response):
        print("after 视图 2")
        return response