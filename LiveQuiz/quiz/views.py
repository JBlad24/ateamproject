# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Quiz index Page")

def join(request):
    return HttpResponse("Enter a code to join a survey")

def displayJoinCode(request):
    return HttpResponse("Visit <join url> and enter the code below to join the survey")
