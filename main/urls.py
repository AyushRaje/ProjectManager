from django.urls import path
from main import views
urlpatterns = [
    path('dashboard/',views.index,name='index'),
    path('addproject',views.create_project,name='create_project'),
    path('joinproject',views.join_pro,name='join_project')
]
