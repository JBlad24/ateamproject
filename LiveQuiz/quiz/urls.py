from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^join/$', views.join, name='join'),
    url(r'^display/$', views.displayJoinCode, name='display')
]