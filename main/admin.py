from django.contrib import admin
from main import models
# Register your models here.

admin.site.register([
    models.Project,
    models.Conversation,
    models.Comment,
    models.Issue,
    models.Members,
    models.Task,
    models.Chat
])