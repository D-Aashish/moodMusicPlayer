from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView    
from .forms import CustomUserCreationForm



class SignUpView(CreateView):
        form_class = CustomUserCreationForm
        success_url = reverse_lazy("")
        template_name = "account/signup.html"

        def form_valid(self, form):
            response = super().form_valid(form)
            user = form.save()
            login(self.request, user)
            return response

class CustomLoginView(LoginView):
    template_name = "account/login.html"

class CustomLogoutView(LogoutView):
    next_page = "/login/" 