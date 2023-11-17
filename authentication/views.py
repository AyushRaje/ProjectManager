from os import name
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.hashers import make_password
# Create your views here.


def signin(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        print(username,"  ",password)
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('index')
        else:
            return redirect('auth')
    return render(request,'auth.html')

def signout(request):
    logout(request)
    return redirect('auth')
        