from main.models import User,Project

def get_available_members(user_id):
    creator = User.objects.get(id=user_id)
    projects = Project.objects.filter(created_by=user_id)
    print(projects)
    members = projects.all()
    all_members=[]
    for obj in members:
        for i in obj.members.all():
            all_members.append({
                "id":i.id,
                "name":i.username
            })
    
    all_members=list(all_members)
    print("members",all_members)
    return all_members