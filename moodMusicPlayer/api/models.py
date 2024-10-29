# from django.db import models

# # Create your models here.
# from mood.models import Mood

# def MoodSelection(request):
#     moods = Mood.objects.values_list('type')

#     if selected_mood:
#         # You can fetch the full mood instance if needed
#         mood_instance = Moods.objects.filter(type=selected_mood).first()
#     else:
#         mood_instance = None

#     return render(request, 'app2/mood_display.html', {'mood': mood_instance})