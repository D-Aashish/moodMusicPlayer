from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration_home, name='registration-home'),
    path('login/', views.registration_loginUser, name='registration-login'),
    path('signup/', views.registration_signupUser, name='registration-signup'),
]