from authentication import models
from django.db import connection
from datetime import datetime
from django.contrib.auth.hashers import make_password,check_password
def create_user(username,email,password):
    with connection.cursor() as cursor:
        try:
            cursor.execute('''
            INSERT INTO auth_user (
            username,email,password,is_superuser,is_staff,is_active,first_name,last_name,date_joined) 
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
            [username,email,make_password(password),False,False,True,'','',datetime.now()])
        
        finally:
            cursor.close()
