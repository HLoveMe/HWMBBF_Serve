from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseBadRequest
from django.db.models import Count

from HMBBF.models import home_ad
from HMBBF.models import home_news
from HMBBF.models import home_Keyword
from HMBBF.models import Guest
from HMBBF.models import Theme
from HMBBF.models import live as Live

from HWHMBBF.models_extension import getReturnJSON
from HWHMBBF.Request_Check import method_check_GET,method_check_POST,User_ID_Check


def testReturn(res,msg="line success  "):
    return JsonResponse({"msg":msg+" : "+str(res)})

#首页数据

@method_check_GET
def home_information(res):
    lan = res.GET.get("lang")
    return JsonResponse({"flag":"success","data":{"ad":getReturnJSON(home_ad.objects.all(),lang=lan),"news":getReturnJSON(home_news.objects.all(),lang=lan)}})


#首页页面得到热词
@method_check_GET
def home_seacher_keyword(res):
    print("========")
    lan = res.GET.get("lang")
    return JsonResponse({"flag":"success","msg":"","data":getReturnJSON(home_Keyword.objects.all(),lang=lan)})


#搜索
@method_check_GET
def home_seacher(res):
    return testReturn(res)
    pass

# 大会议程有多少天
@method_check_GET
def assembly_days(res):
    result  = Theme.objects.values("date").annotate(Count("date"))
    if result is None:
        data = {"flag":"fail"}
    else:
        data = {"flag": "success","msg":""}
        msg=[]
        for one in result:
            time = one["date"].strftime("%m-%d")
            id = len(msg)+1
            msg.append({"id":id,"date":time})
        data["data"]=msg
    return JsonResponse(data)

#得到数据
@method_check_GET
@User_ID_Check
def theme_day(res):
    user_id = 1760
    pars = res.GET if res.method == "GET" else res.POST
    lang = pars.get("lang","zh")
    day = int(pars.get("day","1"))
    sel_result = Theme.objects.values("date").annotate(Count("date"))
    time = sel_result[day-1]["date"].strftime("%Y-%m-%d")
    resu = Theme.objects.filter(date=time)
    data = []
    for i in resu:
        guests = i.theme_guest.all()
        guests_json = getReturnJSON(guests,lang="zh")
        one = i.json()
        one["theme_guest"]=guests_json
        data.append(one)
    return JsonResponse({"status":"success","msg":"","data":data})



#直播数据
@method_check_GET
def live(res):
    print(res.path)
    pars = res.GET
    day = pars.get("day",1)
    print(pars)
    #得到分组shuju
    data = Live.objects.values("date").annotate(Count("date"))
    time = data[int(day)-1]["date"].strftime("%Y-%m-%d")
    data = Live.objects.filter(date=time)
    data = [one.serializa() for one in data]
    json = getReturnJSON(data)
    return JsonResponse({"status":"success","msg":"","data":json})

@method_check_GET
def load_guests(res):
    return  JsonResponse({"status":"success","msg":"","data":getReturnJSON(Guest.objects.all())})