from django.conf.urls import include, url
from django.views.generic import RedirectView
from django.contrib import admin
from .views import index
from HMBBF import urls as home_url
from HMBBF.views import home_seacher
urlpatterns = [
    # Examples:
    # url(r'^$', 'HWHMBBF.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #home
    url(r"^api.php/index/",include(home_url)),

    url(r"^api.php/assembly/index/",RedirectView.as_view(pattern_name="assembly_days")),
    url(r"api.php/assembly/theme/",RedirectView.as_view(pattern_name="theme_day")),
    url(r"api.php/assembly/live/",RedirectView.as_view(pattern_name="theme_live")),
    url(r"api.php/assembly/guest/",RedirectView.as_view(pattern_name="guests_data")),


    url(r"^index/$",index),
]
