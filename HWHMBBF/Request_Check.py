from django.http import HttpResponseBadRequest
import functools

#是否为GET
def method_check_GET(func):
    @functools.wraps(func)
    def warrper(*args,**kwargs):
        res = args[0]
        if (res.method == "POST"):
            return HttpResponseBadRequest("methos POST is error")
        return func(*args,**kwargs)
    return warrper

#是否为POST
def method_check_POST(func):
    @functools.wraps(func)
    def warrper(*args,**kwargs):
        res = args[0]
        if (res.method == "GET"):
            return HttpResponseBadRequest("methos GET is error")
        return func(*args,**kwargs)
    return warrper

#验证USER_ID 是否有效
def User_ID_Check(func):
    @functools.wraps(func)
    def warrper(*args, **kwargs):
        res = args[0]
        pars = res.GET if res.method == "GET" else res.POST
        #  user_id = pars["user_id"]
        # 验证user_id合法性
        #   这里就不做判断
        return func(*args, **kwargs)
    return warrper