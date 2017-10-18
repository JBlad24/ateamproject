# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'quiz/welcome.html')


def student_join(request):
    return render(request, 'quiz/studentJoin.html')


def display_join_url(request):
    return render(request, 'quiz/displayUrl.html')


def create_quiz(request):
    return render(request, 'quiz/createQuiz.html')
