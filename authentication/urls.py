from django.urls import path
from authentication import views

urlpatterns = [
    path('',views.AuthView.as_view(),name='auth_view'),
    path('signup/',views.SignupView,name='signup_view'),
    path('signin/',views.LoginView,name='login_view'),
    path('signout/',views.LogoutView,name='logout_view')
]
