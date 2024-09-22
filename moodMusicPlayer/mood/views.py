from django.shortcuts import render
from .models import Moods
from .forms import MoodsForm

# Create your views here.
def index(request):
    # store_mood= None
        
    if request.method == 'POST':
     form  = MoodsForm(request.POST)
     if form.is_valid():
       moods_list = form.cleaned_data['moods_list']
    #    store_mood = Store.objects.filter()

    # store_mood = Moods.objects.all()
    else:
      form = MoodsForm()

    return render (request, 'mood/index.html', {'form': form})
    # return render (request, 'mood/index.html')