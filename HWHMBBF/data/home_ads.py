import os
import json
# coding:utf-8

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HWHMBBF.settings")

import django
django.setup()
from HMBBF.models import home_ad
path = os.path.dirname(__file__)
path = os.path.join(path,"home_ads.json")
data = json.load(open(path))


for i in range(len(data)):
    oneD = data[i]
    one = home_ad()
    for key in oneD:
        one[key]=oneD[key]
    one.save()



