from main.models import User,Project

def get_available_members(user_id):
    creator = User.objects.get(id=user_id)
    projects = Project.objects.filter(created_by=user_id)
    members = projects.select_related()
    print("memebers",members)