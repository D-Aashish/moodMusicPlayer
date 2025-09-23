import os 

from django.shortcuts import render,redirect
from dotenv import load_dotenv

from .models import Moods
from .forms import MoodsForm

from api.views import getsongView as getsongs
# from api.spotify_utils import store_access_token as storeToken
# from api.spotify_utils import get_token, search_songs

# import requests

load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

def index(request):
    if request.method == 'POST':
        mood = request.POST.get("type")
        if not mood:print("No mood selected!")
        else:print("Mood selected:", mood)

        # token_data = get_token(client_id, client_secret)
        # if token_data:
        #     token = token_data
        #     request.session['spotify_token'] = token
        #     storeToken(token)  # Store the token
            
        form = MoodsForm(request.POST)

        if form.is_valid():
            # mood = form.cleaned_data['type']
            mood_instance = form.save()
            request.session["selected_mood"] = mood_instance.type
            return getsongs(request)
                
        #     else:
        #         print("Form is not valid:", form.errors)
        #         return render(request, 'mood/index.html', {
        #             'form': form,
        #             'error': 'Please select a valid mood.'
        #         })
        
        # else:
        #     print("Failed to retrieve Spotify token.")
        #     return render(request, 'mood/index.html', {
        #         'form': MoodsForm(),
        #         'error': 'Failed to connect to Spotify.'
        #     })
    
    else:
        form = MoodsForm()
        return render(request, 'mood/index.html', {'form': form})

        
def music(request):
    selected_mood = request.session.get('selected_mood', None)
    # token = get_token(client_id, client_secret)
    # if selected_mood:
    #     songs = search_songs(token, selected_mood)
    # else:
    #     songs = []
    return render(request, 'mood/mood_result.html')

def mood_list(request):
    moods = Moods.MOODLIST
    print("mood ",moods)
    return render(request, 'mood/mood_list.html', {'moods': moods})

def mood_view(request):
    if request.method == "POST":
        form = MoodForm(request.POST)  # Process the form with POST data
        if form.is_valid():
            mood = form.cleaned_data['type']
            return render(request, 'mood_result.html', {'mood': mood})
    else:
        form = MoodForm()

    return render(request, 'mood_result.html', {'form': form})