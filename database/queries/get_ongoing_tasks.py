from main.models import Task,User
from django.db import connection
def get_all_ongoing_tasks(user_id):
    with connection.cursor() as cursor:
        try:
            cursor.execute('''
                           SELECT DISTINCT * FROM main_task as m
                           WHERE m.created_by_id = %s AND m.is_active = True
                           ORDER BY m.created_at DESC
                           ''',params=[user_id])
            created_tasks = cursor.fetchall()
            
            cursor.execute('''SELECT * FROM main_task WHERE id=
                           (SELECT task_id FROM main_task_assigned_to as m
                           WHERE m.user_id = %s) AND is_active = True ORDER BY created_at DESC
                           ''',params=[user_id])
            assigned_tasks=cursor.fetchall()
            all_tasks=list(set(assigned_tasks+created_tasks))
            result=[]
            for task in all_tasks:
                task_dict={
                    'title':task[1],
                    'description':task[2],
                    'priority':task[3],
                    'created_at':task[4], 
                    'scheduled_at':task[5]  
                }
                result.append(task_dict)
        except Exception as e:
            print("Exception: "+str(e))
            result=[]
            cursor.close()
            
        finally:
            cursor.close()
        
        return result          