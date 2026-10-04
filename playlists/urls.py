from django.urls import path
from . import views
app_name = 'playlist'

urlpatterns = [
    path('playlist_list/', views.playlist, name='playlist_list'),
    path('playlist/<int:pk>/', views.playlist_detail, name='playlist_detail'),
    path('add/<int:playlist_pk>/<int:track_pk>/', views.add_track_to_playlist, name='add_track'),
    path('delete/<int:playlist_track_pk>/', views.remove_track_from_playlist, name='delete_track'),
]