from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def welcome(request):
    return HttpResponse("<i><b><h1>Welcome Home!</h1></b></i>")
