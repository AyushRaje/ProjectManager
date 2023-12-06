from main.models import User,Project,Issue

def save_issue(user_id,project_id,issue_name,description,assigned_to,priority):
    creator = User.objects.get(id=user_id)
    project = Project.objects.get(id=int(project_id))
    assigned = User.objects.get(id=int(assigned_to))
    issue = Issue.objects.create(created_by=creator,project=project)
    issue.assigned_to.add(assigned)
    issue.name=issue_name
    issue.description=description
    issue.priority=priority
    issue.save()