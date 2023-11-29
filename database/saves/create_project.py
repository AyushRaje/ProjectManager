from main.models import User,Project

def save_project(user_id,unique_id,title,description,additional_details,git_link):
    user = User.objects.get(id=user_id)
    project_created = Project.objects.create(created_by=user)
    project_created.description=description
    project_created.git_link=git_link
    project_created.title=title
    project_created.project_id=unique_id
    project_created.additional_details=additional_details
    project_created.save()
    return project_created.pk
    