from main.models import User,Project

def join_project(user_id,project_id):
    user = User.objects.get(id=user_id)
    project=Project.objects.get(project_id=project_id)
    project.members.add(user)
    project.save()
        
    