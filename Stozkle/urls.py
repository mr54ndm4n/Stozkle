from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.home),
    url(r'^store/', include('myStock.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
    # url(r'^login/', 'django.contrib.auth.views.login'),
    # url(r'login',
    # 	'django.contrib.auth.views.login',
    # 	{'template_name': 'index.html'}
    # 	),
    # url(r'logout',
    # 	'django.contrib.auth.views.logout',
    # 	{'template_name': 'index.html'}
    # 	),
]

urlpatterns += staticfiles_urlpatterns()