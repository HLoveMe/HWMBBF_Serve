from django.contrib import admin

# Register your models here.

from HMBBF import models as home_models



admin.site.register(home_models.home_ad)
admin.site.register(home_models.home_news)
admin.site.register(home_models.home_Keyword)
admin.site.register(home_models.Guest)
admin.site.register(home_models.Theme)
admin.site.register(home_models.live)