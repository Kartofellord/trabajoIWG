from django.http import HttpResponse
from django.shortcuts import render
from .models import userData

# Create your views here.

def mainLogin(request):
    return render(request, "user/login.html")

def signup(request):
    return render(request, "user/signup.html")
 