from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from django.core.validators import MinValueValidator

class Moods(models.Model):
   MOODLIST =  [
    ('HA', 'HAPPY'),
    ('EX', 'EXCITED'),
    ('CA', 'CALM'),
    ('GR', 'GRATEFUL'),
    ('HO', 'HOPEFUL'),
    ('SA', 'SAD'),
    ('AN', 'ANGRY'),
    ('ANX', 'ANXIOUS'),
    ('BO', 'BORED'),
    ('LO', 'LONELY'),
    ('NI', 'INDIFFERENT'),
    ('PE', 'PENSIVE'),
    ('NO', 'NOSTALGIC'),
    ('BI', 'BITTERSWEET'),
    ('AM', 'AMBIVALENT'),
    ('RO', 'ROMANTIC'),
    ('PL', 'PLAYFUL'),
    ('ME', 'MELANCHOLIC'),
    ('MO', 'MOTIVATED'),
    ]
   name = models.CharField(max_length=100)
   upload_date = models.DateTimeField(auto_now_add=True)
   type = models.CharField(max_length=3, choices=MOODLIST)
#    description = models.TextField(default='')                               )

   def __str__(self):
       return self.name
