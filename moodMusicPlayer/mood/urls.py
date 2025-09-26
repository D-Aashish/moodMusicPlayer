from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('music', views.mood_view, name='mood_view'),
    # path('list', views.mood_list, name='mood_list'),
]
