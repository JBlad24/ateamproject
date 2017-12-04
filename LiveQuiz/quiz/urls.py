from django.conf.urls import url

from . import views

app_name = 'quiz'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^join/$', views.student_join, name='join'),
    url(r'^display/(?P<quiz_id>[0-9]+)$', views.display_join_url, name='display'),
    url(r'^create/$', views.create, name='create'),
    url(r'^delete/(?P<quiz_id>[0-9]+)$', views.delete, name='delete'),
    url(r'^createQuiz/$', views.create_quiz, name='create_quiz'),
    url(r'^student/(?P<quiz_id>[0-9]+)/(?P<question_id>[0-9]+)$', views.student_question_view, name='student_question_view'),
    url(r'^teacher/(?P<quiz_id>[0-9]+)/(?P<question_id>[0-9]+)$', views.teacher_question_view, name='teacher_question_view'),
    url(r'^teacher/(?P<quiz_id>[0-9]+)/$', views.teacher_question_help, name='teacher_question_help'),
    url(r'^teacher/results/(?P<quiz_id>[0-9]+)/$', views.quiz_results, name='quiz_results'),
    url(r'^teacherEdit/(?P<quiz_id>[0-9]+)/(?P<question_id>[0-9]+)$', views.teacherEdit_question_view, name='teacherEdit_question_view'),
    url(r'^teacherView/$', views.teacher_view, name='teacher_view'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^(?P<quiz_id>[0-9]+)/detail/$', views.teacher_quiz_view, name='teacher_quiz_view'),
    url(r'^(?P<quiz_id>[0-9]+)/(?P<question_id>[0-9]+)/results/$', views.question_results, name='question_results'),
    url(r'^(?P<quiz_id>[0-9]+)/(?P<question_id>[0-9]+)/results/student/$', views.student_results, name='student_results'),
    url(r'^quizList/$', views.quiz_list_view, name="quiz_list_view"),
    url(r'^(?P<quiz_id>[0-9]+)/(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]