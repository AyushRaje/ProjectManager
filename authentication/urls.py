from django.urls import path
from authentication import views
urlpatterns = [
    path('login/',views.signin,name='auth'),
    path('',views.signout,name='logout')
]
