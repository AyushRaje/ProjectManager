from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
# Create your models here.
class Project(models.Model):
    project_id = models.CharField(max_length=10,unique=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    
    title = models.CharField(max_length=256,null=True,blank=True)
    description= models.CharField(max_length=2048,null=True,blank=True)
    additional_details = models.CharField(max_length=2048,null=True,blank=True)
    git_link = models.CharField(max_length=256,null=True,blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
class Members(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    members = models.ManyToManyField(User)
    
    def __str__(self):
        return self.project.title
    
class Task(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='task_owner')
    assigned_to = models.ManyToManyField(User,related_name='task_assigned_to')
    
    name = models.CharField(max_length=256,null=True,blank=True)
    description = models.CharField(max_length=2048,null=True,blank=True)
    priority = models.CharField(max_length=7,choices=(('high','high'),('medium','medium'),('low','low')),default='low')
    
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_at = models.DateTimeField(null=True,blank=True)
    completed_at = models.DateTimeField(null=True,blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
class Issue(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='issue_owner')
    assigned_to = models.ManyToManyField(User,related_name='issue_assigned_to')
    
    name = models.CharField(max_length=256,null=True,blank=True)
    description = models.CharField(max_length=2048,null=True,blank=True)
    priority = models.CharField(max_length=7,choices=(('high','high'),('medium','medium'),('low','low')),default='low')
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True,blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    task = models.ForeignKey(Task,on_delete=models.CASCADE,null=True,blank=True)
    issue = models.ForeignKey(Issue,on_delete=models.CASCADE,null=True,blank=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    
    description = models.CharField(max_length=2048,null=True,blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.description
    
class Conversation(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='conversation_owner')
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='conversation_receiver',null=True,blank=True)
    
    def __str__(self):
        return str(self.sender.username)
    
    
class Chat(models.Model):
    conversation = models.ForeignKey(User,on_delete=models.CASCADE)
    
    description = models.CharField(max_length=2048,null=True,blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)        
    
    def __str__(self):
        return self.description