from django.urls import path,include
from django.contrib import admin
from .views import SignUpView

urlpatterns = [
    path("", include("django.contrib.auth.urls"), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
