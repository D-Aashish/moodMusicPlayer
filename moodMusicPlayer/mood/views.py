import os 

from django.shortcuts import render,redirect
from dotenv import load_dotenv

from .models import Moods
from .forms import MoodsForm

from api.views import getsongView as getsongs
# from api.spotify_utils import get_songs as getsongs
from api.spotify_utils import get_token, search_songs

# import requests

load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

# Create your views here.
def index(request):
    if request.method == 'POST':
        mood = request.POST.get("type")  # or request.POST["mood"]

        if not mood:
            print("❌ No mood selected!")
        else:
            print("✅ Mood selected:", mood)

        token_data = get_token(client_id, client_secret)
        print("this is client id")
        print(client_id)
        print("this is client secret")
        print(client_secret)

        print("this is token")
        print(token_data)
        print("this is after token")

        form = MoodsForm(request.POST)

        if token_data:
            token = token_data
            request.session['spotify_token'] = token  # Store the token in the session
            form = MoodsForm(request.POST)
            if form.is_valid():
                mood_instance = form.save()
                # store the mood selected in database
                request.session["selected_mood"] = mood_instance.type
                # saves the selected mood type in the session dictionary under the key
                return getsongs(request,token)

            else:
                print("❌ Form is not valid:", form.errors)
                return render(request, 'mood/index.html', {
                    'form': form,
                    'error': 'Please select a valid mood.'
                })
        else:
            # print(token_data)
            # print("this is after token")
            print("❌ Failed to retrieve Spotify token in index view.")
            # Optionally handle the error, e.g., display a message to the user
            return render(request, 'mood/index.html', {'form': MoodsForm(), 'error': 'Failed to connect to Spotify.'})
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
    moods = Moods.MOODLIST
    return render(request, 'mood/mood_list.html', {'moods': moods})
