from main.models import User,Project,Task
import datetime
from dateutil import parser
def save_task(user_id,project_id,task_name,description,assigned_to,schedule_date,schedule_time,priority):
    creator = User.objects.get(id=user_id)
    project = Project.objects.get(id=int(project_id))
    assigned = User.objects.get(id=int(assigned_to))
    task = Task.objects.create(created_by=creator,project=project)
    task.assigned_to.add(assigned)
    task.name=task_name
    task.description=description
    dt=parser.parse(str(schedule_date +" "+schedule_time))
    task.scheduled_at = dt
    task.priority=priority
    task.save()
    
    
