from enum import unique
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control

from database.saves.create_project import save_project
from database.saves.create_member import join_project

from database.queries.get_projects_for_user import get_projects
from database.queries.get_ongoing_tasks import get_all_ongoing_tasks
from database.queries.get_completed_tasks import get_completed_tasks
from database.queries.get_open_issue import get_all_open_issues
from database.queries.get_closed_issue import get_all_closed_issues
from database.queries.get_expired import get_all_expired
from database.queries.get_available_members import get_available_members

import string
import random
 
# initializing size of string

# Create your views here.
UNIQUE_ID=''
def id_generate():
    N = 7
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    return res
@login_required(login_url='/login/')
def index(request):
    user_id = request.user.id
    projects= get_projects(user_id=user_id)
    ongoing_tasks = get_all_ongoing_tasks(user_id=user_id)
    completed_tasks = get_completed_tasks(user_id=user_id)
    open_issues = get_all_open_issues(user_id=user_id)
    closed_issues = get_all_closed_issues(user_id=user_id)
    all_expired = get_all_expired(user_id=user_id)
    unique_id=id_generate()
    UNIQUE_ID=unique_id
    get_available_members(user_id=user_id)
    context={
        'projects':projects,
        'ongoing_tasks':ongoing_tasks,
        'completed_tasks':completed_tasks,
        'open_issues':open_issues,
        'closed_issues':closed_issues,
        'all_expired':all_expired,
        'unique_id':unique_id
    }
    
    # print(completed_tasks)
    return render(request,'index.html',context)

def create_project(request):
    user_id = request.user.id   
    form_data = request.POST
    title=request.POST['title']
    description = request.POST['description']
    git_link = request.POST['git_link']
    add_info={
        'domain':request.POST['domain'],
        'email':request.POST['email_id'],
    }
    if 'dep_link' in form_data.keys():
        dep_link = request.POST['git_link']
        add_info['dep_link']=dep_link
    if 'is_sponsored' in form_data.keys():
        add_info['is_sponsored'] = request.POST['is_sponsored']
        
    if 'is_private' in form_data.keys():
        add_info['dep_link']= request.POST['is_private']       

    project=save_project(user_id=user_id,title=title,description=description,additional_details=add_info,git_link=git_link,unique_id=form_data['action'])    
    print(project)
    
    return redirect('index')
           
def join_pro(request):
    user_id = request.user.id
    if request.method=='POST':
        join_project(user_id=user_id,project_id=request.POST['join_project_id'])
        return redirect('index')          
    return redirect('index')