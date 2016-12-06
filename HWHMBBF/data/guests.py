import os
import json
# coding:utf-8

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HWHMBBF.settings")

import django
django.setup()
from HMBBF.models import Guest
path = os.path.dirname(__file__)
path = os.path.join(path,"guest.json")
data = json.load(open(path))

for i in range(len(data)):
    oneD = data[i]
    one = Guest()
    for key in oneD:
        if(key=="avatar"):
            one[key]=" https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1480667825&di=57000e92a69eefe3b8d36c785e390065&src=http://photocdn.sohu.com/20110419/Img306063524.jpg"
        else:
            one[key]=oneD[key]
    one.save()