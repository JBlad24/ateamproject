# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Quiz, Question, AnswerChoice

# Register your models here.
admin.site.register(Quiz)
# admin.site.register(Question)
# admin.site.register(AnswerChoice)


class ChoiceInline(admin.StackedInline):
    model = AnswerChoice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text']
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)


