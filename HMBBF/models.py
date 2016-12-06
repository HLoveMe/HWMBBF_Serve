# -*- coding:utf-8 -*-
from django.db import models
from django.forms import Form
from django import forms
# Create your models here.


class home_ad(models.Model):
    #
    """
        "ad_name": "华为轮值CEO胡厚崑发布移动宽带X Labs计划 ",
        "ad_name_en": "Three Labs for Building Application-Centric Networks in Three Major Markets",
        "type": "0",
        "target_id": "5",
        "banner_img": "http://huawei.vr68.com/Public/images/upload/5836dfad320e3.jpg",
        "banner_img_en": "http://huawei.vr68.com/Public/images/upload/5837bd8d47837.jpg",
        "ad_url": "http://www.huawei.com/cn/news/2016/11/kenHu-MBBF-XLabs",
        "ad_url_en": "http://www.huawei.com/en/news/2016/11/kenHu-MBBF-XLabs"
    """
    ad_name=models.CharField(u"AD标题",max_length=1024)
    ad_name_en=models.CharField(u"AD_EN_tiitle",max_length=1024)
    type=models.CharField(u"类型",default="0",blank=False,max_length=1024)
    target_id=models.CharField(u"目标ID",blank=False,max_length=1024)
    banner_img=models.CharField(u"图片",max_length=1024)
    banner_img_en = models.CharField(u"EN_图片", max_length=1024)
    ad_url = models.CharField(u"AD_URL",max_length=1024)
    ad_url_en = models.CharField(u"AD_EN_URL", max_length=1024)

    def __setitem__(self, key, value):
        setattr(self,key,value)

    def __unicode__(self):
        return u"首页广告"
    def __str__(self):
        return u"首页广告" + "/" +self.ad_name

class home_news(models.Model):
    title=models.CharField(u"首页新闻",max_length=1024)
    title_en=models.CharField(u"home_title",max_length=1024)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class home_Keyword(models.Model):
    name=models.CharField(u"热词",max_length=256,null=False,blank=False)
    name_en = models.CharField(u"keyword", max_length=256, null=False, blank=False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

#嘉宾
class Guest(models.Model):
    avatar = models.URLField(u"头像")
    guest_name = models.CharField(u"名称",max_length=256)

    company = models.CharField(u"公司",max_length=256)

    position = models.CharField(u"职位",max_length=256)

    is_collect = models.BigIntegerField(default=False,choices=((0,True),(1,False)))

    def __setitem__(self, key, value):
        setattr(self,key,value)

    def __unicode__(self):
        return self.guest_name

    def __str__(self):
        return self.guest_name

#大会
class Theme(models.Model):
    vedio_url=models.CharField(u"视频地址",max_length=256)
    vedio_type=models.CharField(u"类型",max_length=256)
    date = models.DateField(u"时间(哪一天)")
    time_begin = models.TimeField(u"开始时间")  # 9:00
    time_end=models.TimeField(u"结束时间")

    address=models.CharField(u"地点",max_length=256)
    # day=models.IntegerField(u"第几天")

    # type=models.IntegerField(u"类型码")
    type=models.CharField(u"类型",max_length=256,choices=((0,u"峰会演讲(类型码:0)"),(1,u"主题演讲(类型码:1)")),default=0)
    is_collect = models.BooleanField(u"是否收藏",choices=((0,True),(1,False)),default=1)


    # time = models.CharField(u"具体时间段",default=u"不必填写",max_length=256)
    status=models.IntegerField(u"状态",default=0,choices=((0,u"未开始(状态码:0)"),(1,u"进行中(状态码:1)"),(2,u"已结束(状态码:2)"),(3,u"即将开始(状态码:3)"),(4,u"回放(状态码:4)")))
    # status_op=models.CharField(u"状态",max_length=256,choices=((0,u"未开始"),(1,u"进行中"),(2,u"已结束"),(3,u"即将开始"),(4,u"回放")))

    theme_guest = models.ManyToManyField(Guest)

    theme_name=models.CharField(u"名称" , max_length=256)

    def __unicode__(self):
        return self.theme_name

    def __str__(self):
        return self.theme_name


#直播
class live(models.Model):
    live_name=models.CharField(u"名称" , max_length=256)
    time_begin = models.TimeField(u"beigin")
    time_end = models.TimeField(u"end")
    vedio_url = models.TextField(u"URL")
    date=models.DateField(u"日期")

    time = models.TextField(u"时间段",editable=False)

    status = models.IntegerField(u"状态", default=0, choices=(
    (0, u"未开始(状态码:0)"), (1, u"进行中(状态码:1)"), (2, u"已结束(状态码:2)"), (3, u"即将开始(状态码:3)"), (4, u"回放(状态码:4)")))
    type = models.IntegerField(u"类型",choices=((0,u"峰会演讲"),(1,u"主题演讲")))

    is_collect = models.BooleanField(u"是否收藏")

    live_guest = models.ManyToManyField(Guest,blank=True)
    def serializa(self):
        self.time = str(self.time_begin) +"-"+ str(self.time_end)
        self.status_op = {
            0:u"未开始",
            1:u"进行中",
            2:u"已结束",
            3:u"即将开始",
            4:u"回放"
        }[int(self.status)]
        self.type_info= {
            0:u"峰会演讲",
            1:u"主题演讲"
        }[int(self.type)]

        return self

    def __unicode__(self):
        return self.live_name

    def __str__(self):
        return self.live_name
