from django.shortcuts import render,redirect
from .models import Moods
from .forms import MoodsForm
# import requests


# Create your views here.
def index(request):
    # moods = Moods.objects.all()
    if request.method == 'POST':
        form = MoodsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('music')
    else:
        form = MoodsForm()    
    return render(request, 'mood/index.html', {'form': form})
    # return render(request, 'mood/index.html', {'form': form, 'moods': moods})

def music(request):
  return render(request, 'mood/music.html')

def mood_list(request):
    moods = Moods.objects.all()
    return render(request, 'mood/mood_list.html', {'moods': moods})
