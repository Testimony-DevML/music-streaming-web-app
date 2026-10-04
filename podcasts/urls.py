from django.urls import path
from . import views

app_name = 'podcast'

urlpatterns = [
    path('podcast_list/', views.podcast_list, name='podcast_list'),
    path('<int:pk>/', views.podcast_detail, name='podcast_detail'),
]