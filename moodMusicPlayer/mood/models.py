from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Moods(models.Model):
   MOODLIST = {
    'HA': 'Happy',
    'EX': 'Excited',
    'CA': 'Calm',
    'GR': 'Grateful',
    'HOL': 'Hopeful',
    'SA': 'Sad',
    'AN': 'Angry',
    'ANX': 'Anxious',
    'BO': 'Bored',
    'LO': 'Lonely',
    'NI': 'Indifferent',
    'PE': 'Pensive',
    'NO': 'Nostalgic',
    'BI': 'Bittersweet',
    'AM': 'Ambivalent',
    'RO': 'Romantic',
    'PL': 'Playful',
    'ME': 'Melancholic',
    'MO': 'Motivated',
    'FR': 'Frustrated',
    'TI': 'Tiring',
    'EN': 'Energetic',
    'SP': 'Spiritual',
    'EXH': 'Exhilarated',
    'HOS': 'Hopeless',
    'FA': 'Faithful',
    'AW': 'Awkward',
    'CO': 'Confident',
    'SU': 'Surprised',
    'DI': 'Disappointed',
    'FO': 'Forgiving',
}
   name = models.CharField(max_length=100)
   upload_date = models.DateTimeField(auto_now_add=True)
   type = models.CharField(max_length=3, choices=MOODLIST)
#    description = models.TextField(default='')                               )

   def __str__(self):
       return self.name

class TrackPlayed(models.Model):
    track_id = models.CharField(max_length=255)   # or IntegerField if your track.id is int
    image_url = models.URLField()
    audio_url = models.URLField()
    duration = models.FloatField()  # duration in seconds, float allows fractional seconds
    played_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Played Track {self.track_id} at {self.played_at}"