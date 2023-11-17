from os import name
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control
# Create your views here.
@login_required(login_url='/login/')
def index(request):
    return render(request,'index.html')