from django.conf.urls import url
from . import views

urlpatterns = [
    #User Profile
    url(r'^profile/$', views.profile),
    #Store Detail
    url(r'^(?P<equip_id>[0-9]+)/$', views.store_detail),
    #Store List
    url(r'^$', views.store),
]