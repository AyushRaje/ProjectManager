from authentication import models
from django.db import connection
from django.contrib.auth.hashers import make_password,check_password

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

def user_is_valid(email):

    with connection.cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM auth_user WHERE email=%s",[email])
            query_set=cursor.fetchone()
            if query_set:
                return True
            else:
                return False
        finally:
            cursor.close()              