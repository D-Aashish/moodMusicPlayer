from django.urls import path,include
from django.contrib import admin
from .views import *

urlpatterns = [
    # path("", include("django.contrib.auth.urls")),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", CustomLoginView.as_view(), name="login"),
    # path("logout/", CustomLogoutView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
