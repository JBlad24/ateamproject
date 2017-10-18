from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^join/$', views.student_join, name='join'),
    url(r'^display/$', views.display_join_url, name='display'),
    url(r'^createQuiz/$', views.create_quiz, name='create_quiz'),


]