from django.urls import path
from . import views

urlpatterns = [
    path('test', views.index, name='test'),
    path('', views.home, name='home'),
    path('result', views.test2, name='result'),
    path('search/', views.search, name='search'),
    path('recentlyPlayed/', views.recently_played, name='recentlyPlayed'),
    path('bookmarked/', views.bookmarked_song , name='bookmarked_songs'),
    path('trackPlayed/', views.track_played, name='track_played'),
]
