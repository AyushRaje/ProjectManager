from django.urls import path
from authentication import views

urlpatterns = [
    path('',views.AuthView.as_view(),name='auth_view'),
    path('signup/',views.SignupView,name='signup'),
    path('login/',views.LoginView,name='login')
]
