from main.models import User,Issue

def get_all_closed_issues(user_id):
    user = User.objects.get(id=user_id)
    closed_issues = Issue.objects.filter(created_by=user,is_active=False).order_by('-completed_at') | Issue.objects.filter(assigned_to=user,is_active=False).order_by('-completed_at') 
    closed_issues = list(closed_issues.values())
    print(closed_issues)
    return closed_issues