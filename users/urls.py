from django.urls import path
from .views import LogInView, SignUpView, LogOutView

urlpatterns = [
    path('login', LogInView.as_view(), name="loginview"),
    path('signup', SignUpView.as_view(), name="signupview"),
    path('logout', LogOutView.as_view(), name="logoutview")
]