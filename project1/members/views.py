from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")

def profile(request):
    return HttpResponse("Welcome to profile Page")

def school(request):
    return HttpResponse("Welcome to school Page")

def template(request):
    return HttpResponse("Welcome to My tempalate")

def template(request):
    return HttpResponse("Welcome to profile.html")

def template(request):
    return HttpResponse("Welcome to school.html")