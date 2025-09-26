from django.shortcuts import render
from .songs import fetch_songs_from_jamendo as search_songs
from mood.models import Moods

def getsongView(request,mood_instance=None):
    selected_mood_type = request.session.get('selected_mood', None)
    music_info = []
    if selected_mood_type:
        mood_instance = Moods.objects.filter(type=selected_mood_type).first()
        if mood_instance:
            music_info = search_songs(mood_instance.type)
        context = {'musicInfo': music_info}
        return render(request, 'search.html', context)