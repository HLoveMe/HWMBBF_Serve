from django.conf.urls import include, url
from django.contrib import admin
from HMBBF.views import  home_information as information
from HMBBF.views import home_seacher_keyword
from HMBBF.views import home_seacher,assembly_days,theme_day,live,load_guests
urlpatterns = [
    #首页数据
    url(r"index/$",information),
    #首页搜索热词
    url(r"get_keywords/$",home_seacher_keyword),
    #搜索
    url(r"search_result/$",home_seacher),
    #
    url(r"assembly/$",assembly_days,name="assembly_days"),
    url(r"theme/$",theme_day,name="theme_day"),
    url(r"guests/$",load_guests,name="guests_data"),

    url(r"live/$",live,name="theme_live"),
]
