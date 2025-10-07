from django.shortcuts import render
from .songs import fetch_songs_from_jamendo
from .songs import fetch_songs_from_jamendo as search_songs
from mood.models import Moods
from django.http import JsonResponse

def getsongView(request,mood_instance=None):
    selected_mood_type = request.session.get('selected_mood', None)
    music_info = []
    if selected_mood_type:
        mood_instance = Moods.objects.filter(type=selected_mood_type).first()
        if mood_instance:
            music_info = search_songs(mood_instance.type)
            context = {'musicInfo': music_info}
            return render(request, 'mood_result.html', context)
            
    return render(request, 'mood_result.html', {
        'musicInfo': [],
        'error': 'No mood selected.'
    })

def api_get_songs(request):
    mood_query = request.GET.get('mood', '').upper()
    if not mood_query:
        return JsonResponse({'error': 'Mood parameter is empty(from getsongs.py api)'}, status=400)
    songs = fetch_songs_from_jamendo(mood_query)
    # print(f"Fetched songs for mood {songs}")
    if songs:
        return JsonResponse({'songs': songs}, safe=False)
    else:
        return JsonResponse({'error': 'No songs found'}, status=404)
    return JsonResponse({'songs': songs}, safe=False)


    