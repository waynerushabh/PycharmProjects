from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login_module(request):
    return HttpResponse("<h2>You have not logged in yet!</h2>")
