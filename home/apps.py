from django.apps import AppConfig
from queries.tables import *

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
    def ready(self):
        print("Ran function after running server")
        Projects()
        UserJoined()
        print("Created All Databases!")