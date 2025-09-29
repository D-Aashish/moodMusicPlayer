from django.shortcuts import render
from .songs import fetch_songs_from_jamendo as search_songs
from mood.models import Moods
from django.http import JsonResponse
from .songs import fetch_songs_from_jamendo

def getsongView(request,mood_instance=None):
    selected_mood_type = request.session.get('selected_mood', None)
    music_info = []
    if selected_mood_type:
        mood_instance = Moods.objects.filter(type=selected_mood_type).first()

        if mood_instance:
            music_info = search_songs(mood_instance.type)
        context = {'musicInfo': music_info}
        return render(request, 'search.html', context)

        # alternative 
        # if not mood_query:
        #     return JsonResponse({'error': 'Mood parameter is required'}, status=400)

        # # Pass mood_query directly to song fetch function
        # songs = fetch_songs_from_jamendo(mood_query)
        # return JsonResponse({'songs': songs}, safe=False)

    return render(request, 'search.html', {
        'musicInfo': [],
        'error': 'No mood selected.'
    })

def api_get_songs(request):
    mood_query = request.GET.get('mood', '').upper()
    if not mood_query:
        return JsonResponse({'error': 'Mood parameter is empty(from getsongs.py api)'}, status=400)

    # mood_instance = Moods.objects.filter(type=mood_query).first()
    # if not mood_instance:
    #     return JsonResponse({'error': 'Mood not found'}, status=404)
    songs = fetch_songs_from_jamendo(mood_query)
    if songs:
        return JsonResponse({'songs': songs}, safe=False)
    else:
        return JsonResponse({'error': 'No songs found'}, status=404)

    # Return JSON response
    return JsonResponse({'songs': songs}, safe=False)
