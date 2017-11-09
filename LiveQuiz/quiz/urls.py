from django.conf.urls import url

from . import views

app_name = 'quiz'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^join/$', views.student_join, name='join'),
    url(r'^display/$', views.display_join_url, name='display'),
    url(r'^create/$', views.create, name='create'),
    url(r'^createQuiz/$', views.create_quiz, name='create_quiz'),
    url(r'^question[0-9]+(?P<quiz_id>)$', views.student_question_view, name='student_question_view'),
    url(r'^question[0-9]+$', views.teacher_question_view, name='teacher_question_view'),
    url(r'^teacherView/$', views.teacher_view, name='teacher_view'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^(?P<quiz_id>[0-9]+)/detail/$', views.teacher_quiz_view, name='teacher_quiz_view'),
]