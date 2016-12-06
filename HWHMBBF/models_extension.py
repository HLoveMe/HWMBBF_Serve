
# -*- coding:utf-8 -*-
from django.db import models
#模型json
def json(self,lang="zh"):
    dic = self.__dict__
    try:
        dic.pop("_state")
    except:
        pass
    result={}

    # {key:value for (key,value) in dic.items() if key.__contains__("_EN")}
    keys = [key for (key,value) in dic.items() if key.endswith("_en")]
    #[name_en,img_en]
    for key in keys:
        if(lang == "en"):
            try:
                dic.pop(key[0:-3])
            except:
                print("===================")
                print(key + ":" +"命名有误/"+"    exam: name(name_en)")
                print("===================")
        else:
            dic.pop(key)

    return  dic

#单个对象JSON 化
models.Model.json = json


#数据JSON 话
def getReturnJSON(objs,lang="zh"):
    if isinstance(objs,dict) and isinstance(objs,models.Model):
        return  objs.json(lang=lang)
    else:
        result = []
        for i in range(len(objs)):
            one = objs[i]
            if(isinstance(one,models.Model)):
                result.append(one.json(lang=lang))
        return result
