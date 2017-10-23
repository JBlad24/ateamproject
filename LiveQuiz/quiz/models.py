# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models


# Create your models here.
class Quiz(models.Model):
    quiz_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.quiz_name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=300)

    def __str__(self):
        return self.question_text


class AnswerChoice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


