from django.db import connection

def Projects():
    try:
        with connection.cursor() as cursor:
            cursor.execute('''CREATE TABLE IF NOT EXISTS projects(
                        project_id INT NOT NULL PRIMARY KEY,
                        project_name VARCHAR(256) NOT NULL,
                        created_at DATETIME NOT NULL,
                        created_by VARCHAR(256) NOT NULL,
                        FOREIGN KEY (created_by) REFERENCES auth_user(username)      
            )''')
            
    except Exception as e:
        print("Exception :",str(e))

    finally:
        cursor.close()
def UserJoined():
    try:
        with connection.cursor() as cursor:
            cursor.execute('''CREATE TABLE IF NOT EXISTS user_joined(
                              project_id INT NOT NULL AUTOINCREMENT,
                              user VARCHAR(256) NOT NULL,
                              FOREIGN KEY (project_id) REFERENCES projects(project_id),
                              FOREIGN KEY (user) REFERENCES auth_user(username)
                              PRIMARY KEY (project_id, user)
            )''')      
    except Exception as e:
        print("Exception :",str(e))

    finally:
        cursor.close()        

def AlterTable():
    with connection.cursor() as cursor:
         cursor.execute('''ALTER TABLE user_joined MODIFY(
                              project_id INT NOT NULL,
                              user VARCHAR(256) NOT NULL,
                              FOREIGN KEY (project_id) REFERENCES projects(project_id),
                              FOREIGN KEY (user) REFERENCES auth_user(username)
                              PRIMARY KEY (project_id, user)
            )''')
         cursor.execute('''ALTER TABLE projects MODIFY(
                        project_id INT NOT NULL PRIMARY KEY,
                        project_name VARCHAR(256) NOT NULL,
                        created_at DATETIME NOT NULL,
                        created_by VARCHAR(256) NOT NULL,
                        FOREIGN KEY (created_by) REFERENCES auth_user(username)      
            )''')
         cursor.close()         

def DropTable():
    with connection.cursor() as cursor:
         cursor.execute('''DROP TABLE user_joined
            ''')
         cursor.execute('''DROP TABLE projects
            ''')
         cursor.close()