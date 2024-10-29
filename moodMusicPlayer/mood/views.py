from django.shortcuts import render,redirect
from .models import Moods
from .forms import MoodsForm
from api.spotify_utils import get_songs, get_token, search_songs
from api.views import get_songs
from dotenv import load_dotenv
import os 
# import requests

load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

# Create your views here.
def index(request):
    # moods = Moods.objects.all()
    # selected_mood = request.session.get('selected_mood', None)
    token = get_token(client_id, client_secret)
    if request.method == 'POST':
        form = MoodsForm(request.POST)
        if form.is_valid():
            mood_instance = form.save()
            request.session["selected_mood"] = mood_instance.type
            # return redirect('get_songs()')
    else:
        form = MoodsForm()    
    return render(request, 'mood/index.html', {'form': form})
    # return render(request, 'mood/index.html', {'form': form, 'moods': moods})

def music(request):
    selected_mood = request.session.get('selected_mood', None)
    token = get_token(client_id, client_secret)
    if selected_mood:
        # Use selected_mood for your logic, e.g., search for songs
        songs = search_songs(token, selected_mood)  # Assuming you have a token available
    else:
        songs = []
    return render(request, 'mood/mood_result.html')

def mood_list(request):
    moods = Moods.objects.all()
    return render(request, 'mood/mood_list.html', {'moods': moods})
