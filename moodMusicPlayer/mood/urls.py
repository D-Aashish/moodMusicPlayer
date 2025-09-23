from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('music', views.music, name='music'),
    path('mv', views.music, name='mood_view'),
    path('list', views.mood_list, name='mood_list'),
    # path('admin/', admin.site.urls),

]
