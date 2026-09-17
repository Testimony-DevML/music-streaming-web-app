from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('music_list/', views.music_list, name='music_list')
]