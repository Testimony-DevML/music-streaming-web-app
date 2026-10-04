from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('music_list/', views.music_list, name='music_list'),
    path('recently_played/<int:track_pk>/', views.recently_played, name='record_recently_played'),
    path('saved_position/<int:track_pk>/', views.saved_position, name='saved_position'),
    # path('resume_position/<int:track_pk>/', views.resume_position, name='resume_position'),
    path('recently_played_list/', views.recently_played_list, name='recently_played_list'),
    path('favorite/<int:track_pk>/', views.toggle_favorite, name='toggle_favorite'),
    path('favorite_list/', views.favorite_list, name='favorite_list'),
    path('search/', views.search, name='search'),
]