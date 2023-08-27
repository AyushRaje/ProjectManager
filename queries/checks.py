from authentication import models
from django.db import connection

def user_already_exists(email):

    with connection.cursor() as cursor:
        try:
            cursor.execute("SELECT email FROM auth_user WHERE email=%s",[email])
            query_set=cursor.fetchone()
            if query_set:
                return True
            else:
                return False
        finally:
            cursor.close()    

def user_is_valid(username,password):

    with connection.cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM auth_user WHERE username=%s AND password=%s",[username,password])
            query_set=cursor.fetchone()
            if query_set:
                return True
            else:
                return False
        finally:
            cursor.close()              