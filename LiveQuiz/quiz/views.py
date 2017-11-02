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
    quiz_name = request.POST['quizname']
    questions = request.POST.getlist("questions[]")

    new_quiz = Quiz()
    new_quiz.quiz_name = quiz_name
    new_quiz.save()

    for idx, question in enumerate(questions):
        new_question = Question(question_text=question)
        new_question.quiz = new_quiz
        new_question.save()
        answer_choices = request.POST.getlist("answerChoices[]" + str(idx+1))
        for choice in answer_choices:
            new_choice = AnswerChoice(choice_text=choice, votes=0)
            new_choice.question = new_question
            new_choice.save()

    return HttpResponseRedirect(reverse('quiz:index'))

def student_question_view(request):
    return render(request, r'quiz/studentQuestionView.html')
