from django import forms
from  .models import Moods

class MoodsForm(forms.Form):
    moods_list= forms.ModelChoiceField(queryset=Moods.objects.all())