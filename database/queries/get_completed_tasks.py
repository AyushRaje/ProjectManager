from main.models import Task,Project
from django.contrib.auth.models import User

def get_completed_tasks(user_id):
    user = User.objects.get(id=user_id)
    completed_tasks = Task.objects.filter(created_by=user,is_active=False).order_by('-completed_at') | Task.objects.filter(assigned_to=user,is_active=False).order_by('-completed_at')
    completed_tasks = list(completed_tasks.values())
    return completed_tasks
    