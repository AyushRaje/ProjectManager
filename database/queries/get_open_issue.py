from main.models import User,Issue

def get_all_open_issues(user_id):
    user = User.objects.get(id=user_id)
    open_issues = Issue.objects.filter(created_by=user,is_active=True).order_by('-created_at') | Issue.objects.filter(assigned_to=user,is_active=True).order_by('-created_at')
    open_issues = list(open_issues.values())
    print(open_issues)
    return open_issues