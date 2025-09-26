import os 
from django.shortcuts import render,redirect
from dotenv import load_dotenv
from .models import Moods
from .forms import MoodsForm
from api.views import getsongView as getsongs
load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

def index(request):
    if request.method == 'POST':
        form = MoodsForm(request.POST)
        if form.is_valid():
            mood_instance = form.save()
            request.session["selected_mood"] = mood_instance.type
            return getsongs(request,mood_instance)  
        else:
            print("Form is not valid:", form.errors)
            return render(request, 'index.html', {
                    'form': form,
                    'error': 'Please select a valid mood.'
                })
    else:
        form = MoodsForm()
        return render(request, 'index.html', {'form': form})

def mood_view(request):
    if request.method == "POST":
        form = MoodForm(request.POST)
        if form.is_valid():
            mood = form.cleaned_data['type']
            return render(request, 'mood_result.html', {'mood': mood})
    else:
        form = MoodForm()
    return render(request, 'mood_result.html', {'form': form})