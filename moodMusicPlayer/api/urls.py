from django.urls import path
# from .views import *
from .import views 

urlpatterns = [
        path('', views.api_get_songs, name='api_get_songs'),
]
