# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
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
    questions = Question.objects.all()
    return render(request, r'quiz/studentQuestionView.html', {'questions', questions})


def teacher_view(request):
    return render(request, 'quiz/teacherView.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('quiz:index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})