from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from queries import (
    checks,
    create
)
from authentication import models
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
# Create your views here.

class AuthView(TemplateView):
    template_name='auth.html'

    def get(self,request):
        return render(request,'auth.html')
    
def SignupView(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['pass']
        cnfpassword=request.POST['cnfpass']
        username=str(email).split('@')[0]

        if checks.user_already_exists(email):
            messages.info(request,"User Already Exists")
            return redirect('auth_view')
        else:
            if cnfpassword==password:
                create.create_user(username,email,password)
                messages.success(request,"Signedup Successfully")
                return redirect('auth_view')
            
            else:
                messages.info(request,"Please Enter Same Password")
                return redirect('auth_view')


    return render(request,'auth.html')

def LoginView(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['pass']
        username=str(email).split('@')[0]

        if checks.user_is_valid(username,password):
            user=authenticate(request,username=username,password=password)
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,"Please Enter Correct Credentials")
            return redirect('auth_view')
        

                       