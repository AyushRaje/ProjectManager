from main.models import User,Project
from django.db import connection
def get_projects(user_id):
    
    
    with connection.cursor() as cursor:
        try:
            #created_projects
            projects=[]
            cursor.execute('SELECT * FROM auth_user WHERE id=%s',params=[user_id])
            user = cursor.fetchone()
            # print(user)
            cursor.execute('''SELECT * FROM main_project as p WHERE created_by_id=%s''',params=[user_id])
            created_projects = cursor.fetchall()
            print(created_projects)
            
            #joined projects
            cursor.execute('''SELECT * FROM main_project as p
                           WHERE id = (SELECT project_id FROM
                           main_members m WHERE m.id=(SELECT members_id
                           FROM main_members_members
                           WHERE user_id=%s))''',params=[user_id])
            joined_projects=cursor.fetchall()
            print(joined_projects)
            for p in created_projects:
                project_dict={
                    'project_id':p[1],
                }
            
            
            
        except Exception as e:
            print("Exception :"+str(e))    
            created_projects=[]
            joined_projects=[]
        
        finally:
            cursor.close()
                
        return created_projects,joined_projects    