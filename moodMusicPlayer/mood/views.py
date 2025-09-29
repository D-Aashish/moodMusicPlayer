from django.shortcuts import render,redirect
from .models import Moods
from .forms import MoodsForm
from api.views import getsongView as getsongs
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
                # return getsongs(request,mood_instance)  
            else:
                print("Form is not valid:", form.errors)
                return render(request, 'index.html', {
                        'form': form,
                        'error': 'Please select a valid mood.'})
    else:
        form = MoodsForm()
        return render(request, 'index.html', {'form': form})

def mood_view(request):
    if request.method == "POST":
        form = MoodForm(request.POST)
        if form.is_valid():
            mood = form.cleaned_data['type']
            return render(request, 'mood_result.html', {'mood': mood})
    else:
        form = MoodForm()
    return render(request, 'mood_result.html', {'form': form})

def test(request):
    return render(request, "temp.html")