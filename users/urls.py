from django.urls import path
from .views import LogInView, SignUpView

urlpatterns = [
    path('login', LogInView.as_view(), name="loginview"),
    path('signup', SignUpView.as_view(), name="signupview"),
]