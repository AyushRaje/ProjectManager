from django.urls import path
from main import views
urlpatterns = [
    path('dashboard/',views.index,name='index')
]
