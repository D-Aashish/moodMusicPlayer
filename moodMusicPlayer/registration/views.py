from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def loginUser(request):
    if request.method == "POST":
        username = request.POST["inputUsername"]
        password = request.POST["inputPassword"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error("login failed")
            # return redirect('login')
            return redirect('login')
    else:
        return render(request,'registration/login.html')

def signupUser(request):
    return render(request, 'registration/signup.html', {})

def home(request):
    return render(request, 'registration/home.html')