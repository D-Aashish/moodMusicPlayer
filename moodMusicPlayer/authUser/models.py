from django.db import models
from django.contrib.auth.models import AbstractUser
from mood.models import BookMarkedSong

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True,max_length=100)
    password = models.CharField(max_length=100)
    # bookmarked_songs = models.ManyToManyField(BookMarkedSong, through='mood.UserBookmarkedSong')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']