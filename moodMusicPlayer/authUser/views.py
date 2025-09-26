from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login



class SignUpView(CreateView):
        form_class = UserCreationForm
        success_url = reverse_lazy("mood:index")
        template_name = "registration/signup.html"

        def form_valid(self, form):
            response = super().form_valid(form)
            user = form.save()
            login(self.request, user)
            return response
