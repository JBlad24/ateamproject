# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Quiz, Question, AnswerChoice


# Create your views here.
def index(request):
    return render(request, 'quiz/index.html')


def student_join(request):

    return render(request, 'quiz/studentJoin.html')


def display_join_url(request):
    return render(request, 'quiz/displayUrl.html')


def create(request):
    return render(request, 'quiz/create.html')


def create_quiz(request):

    new_quiz = Quiz(quiz_name='test123')
    new_quiz.save()
    new_quiz.question_set.create(question_text='Is this working')

    return HttpResponseRedirect(reverse('quiz:index'))


