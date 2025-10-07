from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Moods, TrackPlayed
from .forms import MoodsForm
from api.views import getsongView as getsongs
from api.songs import getTopArtist, mostPlayedSongs
from api.songs import fetch_songs_from_jamendo as search_songs
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    print("POST data:", request.POST)
    if request.method == 'POST':
        action = request.POST.get('action')
        print("Action received:", action)
        if action == 'logout':
            logout(request)
            return redirect('login') 
        elif action == 'mood':
            form = MoodsForm(request.POST)
            print("This is form :",form)
            if form.is_valid():
                print("form is valid")
                mood_instance = form.save()
                request.session["selected_mood"] = mood_instance.type
                songs = getsongs(request,mood_instance)  
                return songs
            else:
                print("Form is not valid:", form.errors)
                return render(request, 'index.html', {
                        'form': form,
                        'error': 'Please select a valid mood.'})
    else:
        form = MoodsForm()
        return render(request, 'index.html', {'form': form})


def home(request):
    Artists = getTopArtist()
    MostPlayedSongs = mostPlayedSongs()
    played_track = TrackPlayed.objects.order_by('-played_at').first()
    print("This is playing right now ",played_track)
    return render(request, "home.html",{ 'Artists':Artists, 'MostlyPlayed':MostPlayedSongs, 'PlayedTrack': played_track })

def test2(request):
    return render(request, "mood_result.html")


@csrf_exempt  # only if you can't set CSRF token properly — better to handle CSRF properly!
def track_played(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            track_id = data.get('track_id')
            image_url = data.get('image_url')
            audio_url = data.get('audio_url')
            duration = data.get('duration') or 0.0 

            # You can save to your DB here. For now just print/log
            print(f"Track Played: ID={track_id}, Image={image_url}, Audio={audio_url}, Duration={duration}")
            played_track = TrackPlayed.objects.create(
                track_id=track_id,
                image_url=image_url,
                audio_url=audio_url,
                duration=duration
            )

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)


def search(request):
    mood = request.GET.get('mood')
    print("mood:", mood)
    if not mood:
        print("mood inside if :", mood)
        return render(request, 'mood_result.html', {'error': 'No mood provided.'})
    print("stating mood song selection")
    try:
        print("stating mood song selection inside try")
        music_info = search_songs(mood)
        print("search songs complete")
        context = {'musicInfo': music_info}
        # print("stating mood song selection")
        print("songs obatinaed from search_songs: ", context)
        return render(request, 'mood_result.html', context)
        # return render(request, 'mood_result.html',{'Songs':songs})
    except Exception:
        print("stating mood  inside except")
        songs = []
        return render(request, 'mood_result.html', {'error': 'no songs found.'})
    