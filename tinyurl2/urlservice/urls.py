from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from . import views

## fix http server failed to find static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^encode/$', views.encode, name='encode'),
    url(r'^user/(\w+)', views.profile, name='profile'), # capture a word of any length, so it will capture a username
    url(r'^login/$', views.login_view, name='login'), # we cannot name our view login because there's a built-in login function
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^(\w+)/$', views.decode, name='decode'),
]

urlpatterns += staticfiles_urlpatterns()
