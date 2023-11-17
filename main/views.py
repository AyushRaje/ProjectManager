from os import name
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control
from database.queries.get_projects_for_user import get_projects
# Create your views here.
@login_required(login_url='/login/')
def index(request):
    user_id = request.user.id
    created_projects,joined_projects= get_projects(user_id=user_id)
    
    return render(request,'index.html')