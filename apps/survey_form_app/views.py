# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):

    return render(request, "survey_form_app/index.html")

def submit(request):
    if request.method == "POST":
        print "*" * 50
        print request.POST
        print request.POST['name']
        print request.POST['city']
        print request.POST['language']
        print request.POST['comment']

    return render(request, "survey_form_app/index.html")
