from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

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
   name = models.CharField(max_length=100, db_index=True)
   type = models.CharField(max_length=3, choices=MOODLIST, db_index=True)
   upload_date = models.DateTimeField(auto_now_add=True, db_index=True)
#    description = models.TextField(default='')                               )

   def __str__(self):
       return self.name

class TrackPlayed(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    track_id = models.CharField(max_length=255, db_index=True)
    played_at = models.DateTimeField(auto_now_add=True, db_index=True)
    image_url = models.URLField()
    audio_url = models.URLField()
    duration = models.FloatField()

    def __str__(self):
        return f"Played Track {self.track_id} at {self.played_at}"

class BookMarkedSong(models.Model):
    track_id = models.CharField(max_length=255, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    image_url = models.URLField()
    audio_url = models.URLField()
    duration = models.FloatField()
    played_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.track_id}"

class UserBookmarkedSong(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    song = models.ForeignKey(BookMarkedSong, on_delete=models.CASCADE)
    bookmarked_at = models.DateTimeField(auto_now_add=True, db_index=True)

