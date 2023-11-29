from main.models import User,Task
import datetime
from django.utils import datetime_safe,timezone
def get_all_expired(user_id):
    user = User.objects.get(id=user_id)
    expired = Task.objects.filter(created_by=user,is_active=True)
    expired = list(expired.values())
    all_expired=[]
  
    for exp in expired:
        if exp['scheduled_at'] < datetime.datetime.now(tz=datetime.timezone.utc):
            all_expired.append(exp)        
    print(all_expired)
    print(datetime.datetime.now(tz=datetime.timezone.utc))
    return all_expired        