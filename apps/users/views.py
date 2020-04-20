from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
#user_dashboard

def index(request):
    return render(request, 'users/index.html')

def new(request):
    return render(request, 'users/new.html')

def signin(request):
    return render(request, 'users/signin.html')  

def register(request):
    return render(request, 'users/register.html')

def edit(request):
    return render(request, 'users/edit.html')

def dashboard(request):
    return render(request, 'users/dashboard.html')              