# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Quiz, Question, AnswerChoice


# Create your views here.
def index(request):
    return render(request, 'quiz/index.html')


def student_join(request):
    # quiz_id = request.POST.get("code")
    # print(quiz_id)
    # quiz = Quiz.objects.get(pk=quiz_id)
    # question_id = quiz.questions.first().id

    return render(request, 'quiz/studentJoin.html')


def display_join_url(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    questions = quiz.questions.all()

    for question in questions:
        answers = question.answers.all()
        for answer in answers:
            answer.votes = 0
            answer.save()

    return render(request, 'quiz/displayUrl.html', {'quiz_id': quiz_id})


def create(request):
    return render(request, 'quiz/create.html')


def create_quiz(request):
    quiz_name = request.POST['quizname']
    questions = request.POST.getlist("questions[]")

    new_quiz = Quiz()
    new_quiz.quiz_name = quiz_name
    new_quiz.teacher = request.user
    new_quiz.save()

    for idx, question in enumerate(questions):
        new_question = Question(question_text=question)
        new_question.quiz = new_quiz
        new_question.save()
        answer_choices = request.POST.getlist("answerChoices[]" + str(idx + 1))
        for choice in answer_choices:
            new_choice = AnswerChoice(choice_text=choice, votes=0)
            new_choice.question = new_question
            new_choice.save()

    return HttpResponseRedirect(reverse('quiz:teacher_view'))


def edit_question(request):
    quiz_id = request.POST['quizId']
    question_id = request.POST['questionId']
    quiz = Quiz.objects.get(pk=quiz_id)
    question = Question.objects.get(pk=question_id)
    question.question_text = request.POST['questionText']

    answerList = question.answers.all()
    answer_choices = request.POST.getlist("answers[]")

    count = 0
    for answer in answerList:
        answer.choice_text = answer_choices[count]
        answer.save()
        count += 1

    question.save()

    return redirect("/quiz/teacher/" + quiz_id + "/" + question_id)


def student_question_view(request, quiz_id, question_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    question = quiz.questions.get(pk=question_id)
    return render(request, r'quiz/studentQuestionView.html', {'quiz': quiz, 'question': question})


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
            return redirect('quiz:teacher_view')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def teacher_quiz_view(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = quiz.questions.all()

    return render(request, 'quiz/teacherQuizView.html', {'quiz': quiz})


def teacher_question_view(request, quiz_id, question_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    question = quiz.questions.get(pk=question_id)
    return render(request, 'quiz/teacherQuestionView.html', {'question': question, 'quiz_id': quiz_id})


def teacherEdit_question_view(request, quiz_id, question_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    question = quiz.questions.get(pk=question_id)
    return render(request, 'quiz/teacherEdit.html', {'question': question, 'quiz_id': quiz_id})


def quiz_list_view(request):
    quizzes = Quiz.objects.filter(teacher=request.user)

    return render(request, 'quiz/quizListView.html', {'quizzes': quizzes})


def question_results(request, quiz_id, question_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    question = get_object_or_404(Question, pk=question_id)

    # get the id of the last question in the quiz
    last_id = quiz.questions.all().last().id
    return render(request, 'quiz/teacherQuestionResults.html',
                  {'question': question, 'quiz_id': quiz_id, 'last_id': last_id})


def student_results(request, quiz_id, question_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    question = get_object_or_404(Question, pk=question_id)

    # get the id of the last question in the quiz
    last_id = quiz.questions.all().last().id
    return render(request, 'quiz/studentQuestionResults.html',
                  {'question': question, 'quiz_id': quiz_id, 'last_id': last_id})


def teacher_question_help(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    first_id = quiz.questions.all().first().id
    return redirect('/quiz/teacher/' + str(quiz_id) + '/' + str(first_id))


def quiz_results(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    return render(request, 'quiz/quizResults.html', {'quiz': quiz})


def quiz_student_results(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    return render(request, 'quiz/quizStudentResults.html', {'quiz': quiz})


def delete(request, quiz_id):
    Quiz.objects.filter(id=quiz_id).delete()
    return HttpResponseRedirect(reverse('quiz:quiz_list_view'))


def student_question_view_help(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    first_id = quiz.questions.all().first().id
    return redirect('/quiz/student/' + str(quiz_id) + '/' + str(first_id))


def vote(request, quiz_id, question_id):
    # quiz = get_object_or_404(Quiz, pk=quiz_id)
    question = get_object_or_404(Question, pk=question_id)
    selected_answer = question.answers.get(pk=request.POST['answer'])
    selected_answer.votes += 1
    selected_answer.save()
    return HttpResponseRedirect('/quiz/' + quiz_id + '/' + question_id + '/results/student/', )
