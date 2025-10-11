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
from django.core.cache import cache

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
    Artists = cache.get('artists')
    MostPlayedSongs = cache.get('most_played_songs')

    if not Artists:
        Artists = getTopArtist()
        cache.set('artists', Artists, timeout=900)
    
    if not MostPlayedSongs:
        MostPlayedSongs = mostPlayedSongs()
        cache.set('most_played_songs', MostPlayedSongs, timeout=2000)

    now_playing = request.session.get('now_playing')

    if now_playing:
        played_track = now_playing
    else:
        played_track = TrackPlayed.objects.order_by('-played_at').first()

    return render(request, "home.html",{ 'Artists':Artists, 'MostlyPlayed':MostPlayedSongs, 'PlayedTrack': played_track })

def test2(request):
    return render(request, "mood_result.html")


@csrf_exempt
def track_played(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            track_id = data.get('track_id')
            image_url = data.get('image_url')
            audio_url = data.get('audio_url')
            duration = data.get('duration') or 0.0 

            print(f"Track Played: ID={track_id}, Image={image_url}, Audio={audio_url}, Duration={duration}")
            played_track = TrackPlayed.objects.create(
                track_id=track_id,
                image_url=image_url,
                audio_url=audio_url,
                duration=duration
            )

            request.session['now_playing'] = {
                'track_id': track_id,
                'image_url': image_url,
                'audio_url': audio_url,
                'duration': duration,
            }

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
    cache_key = f'mood-_{mood.lower()}'
    music_info = cache.get(cache_key)
    
    if music_info:
        print(f"Using cached results for mood: {mood}")
        cache.get()
    else:
        print(f"Fetching new results for mood: {mood}")
        try:
            print("stating mood song selection inside try")
            music_info = search_songs(mood)
            print("search songs complete")
            # request.session['search_results'] = music_info
            # cache.set(cache_key, music_info, timeout=300)/
            cache.set(cache_key, music_info, timeout=900)
            print("Search songs complete and cached.")

            context = {'musicInfo': music_info}
            # print("songs obatinaed from search_songs: ", context)
            # return render(request, 'mood_result.html', context)
        except Exception:
            print("stating mood  inside except")
            songs = []
            return render(request, 'mood_result.html', {'error': 'no songs found.'})

    context = {'musicInfo': music_info}
    print("Returning context:", context)
    return render(request, 'mood_result.html', context)    