import os
import json
import django
from django.db.models import QuerySet,Count
from django.db import transaction
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HWHMBBF.settings")

django.setup()
from HMBBF.models import Guest
from HMBBF.models import Theme


path = os.path.dirname(__file__)
path = os.path.join(path,"themes.json")

datas = json.load(open(path))

@transaction.atomic()
def save():
    Theme.objects.all().delete()
    for data in datas:
        one = Theme()
        one.vedio_url = data["vedio_url"]
        one.vedio_type = data["vedio_type"]
        one.date = data["date"]
        one.time_begin = data["time_begin"]
        one.time_end = data["time_end"]
        one.address = data["address"]
        one.type_info = 1 if data["type_info"]=="主题演讲" else 0
        one.is_collect = data["is_collect"]
        one.status = data["status"]
        one.id=data["id"]
        one.theme_name = data["theme_name"]
        guests = []
        print("==========")
        for guest in data["theme_guest"]:
            ID = guest["guest_id"]
            gu = Guest.objects.filter(id=ID).all().first()
            print(gu)
            if gu == None:
                gu = Guest()
                gu.id = guest["guest_id"]
                gu.avatar = guest["avatar"]
                gu.guest_name=guest["guest_name"]
                gu.company = guest["company"]
                gu.company= guest["position"]
                print(gu)
                gu.save()

            guests.append(gu)
        one.save()
        for i in guests:
            one.theme_guest.add(i)
            one.save()
save()