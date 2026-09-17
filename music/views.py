from django.shortcuts import render
from .models import Track
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def music_list(request):
    tracks = Track.objects.all() 

    genre = request.GET.get('genre', 'All')
    if genre != 'All':
        tracks = tracks.filter(genre__iexact=genre)

    return render(request, 'music/music_list.html', {'tracks': tracks, 'genre':genre})

   

