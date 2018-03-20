# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    return render(request, "survey_form_app/index.html")

def submit(request):
    if request.method == "POST":
        request.session['count'] = request.session['count'] + 1
        request.session['name'] = request.POST['name']
        request.session['city'] = request.POST['city']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
    count = {
        "count" : request.session['count']
    }

    return render(request, "survey_form_app/display.html", count)
