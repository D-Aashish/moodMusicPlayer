from django.shortcuts import render,redirect
from .models import Moods
from .forms import MoodsForm
from api.views import getsongView as getsongs
from api.songs import getTopArtist
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    print("POST data:", request.POST)
    if request.method == 'POST':
        action = request.POST.get('action')
        print("Action received:", action)
        if action == 'logout':
            logout(request)
            return redirect('login') 
        elif action == 'mood':
            form = MoodsForm(request.POST)
            print("This is form :",form)
            if form.is_valid():
                print("form is valid")
                mood_instance = form.save()
                request.session["selected_mood"] = mood_instance.type
                songs = getsongs(request,mood_instance)  
                return songs
            else:
                print("Form is not valid:", form.errors)
                return render(request, 'index.html', {
                        'form': form,
                        'error': 'Please select a valid mood.'})
    else:
        form = MoodsForm()
        return render(request, 'index.html', {'form': form})


def home(request):
    Artists = getTopArtist()
    return render(request, "home.html",{'Artists':Artists})
def test2(request):
    return render(request, "mood_result.html")

def search(request):
    mood = request.GET.get('mood')
    if not mood:
        return render(request, 'mood_result.html', {'error': 'No mood provided.'})
    try:
        songs = getsongs(request,mood)
        # print("songs : ", songs)
        return render(request, 'mood_result.html', {'mood': mood})
        # return songs
    except Exception:
        songs = []
        return render(request, 'mood_result.html', {'error': 'no songs found.'})
    
def topArtist(request):
    ()
    return render(request, "home.html", {'Artists':Artists})