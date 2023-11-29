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
            cursor.execute('''SELECT * FROM main_project as p WHERE created_by_id=%s ORDER BY p.created_at DESC''',params=[user_id])
            created_projects = cursor.fetchall()
            # print(created_projects)
            
            #joined projects
            cursor.execute('''SELECT * FROM main_project as p
                           WHERE id = (SELECT project_id FROM
                           main_project_members m WHERE m.id=%s
                           ) AND p.is_active=True ORDER BY p.created_at DESC''',params=[user_id])
            joined_projects=cursor.fetchall()
            # print(joined_projects)
            for p in created_projects:
                project_dict={
                    'id':p[0],
                    'project_id':p[1],
                    'title':p[2],
                    'description':p[3][0:30],
                    'created_at':p[6]
                }
                projects.append(project_dict)
            for p in joined_projects:        
                project_dict={
                    'id':p[0],
                    'project_id':p[1],
                    'title':p[2],
                    'description':p[3][0:30],
                    'created_at':p[6]
                }
                projects.append(project_dict)    
            print(projects)
            
        except Exception as e:
            print("Exception :"+str(e))    
            projects=[]
        
        finally:
            cursor.close()
                
        return projects 