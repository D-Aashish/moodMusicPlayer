from django import forms
from  .models import Moods

moods_list= forms.ModelChoiceField(queryset=Moods.objects.all())

class MoodsForm(forms.ModelForm):
    class Meta:
        model = Moods
        # fields = ['name', 'type']  # Include fields you want in the form
        fields = ['type']
        widgets = {
            # 'name': forms.TextInput(attrs={'placeholder': 'Enter your mood name'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            # 'name': 'Mood Name',
            'type': 'Select Mood',
        }       