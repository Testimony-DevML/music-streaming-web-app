from django.shortcuts import render, redirect, get_object_or_404
from .models import Playlist, PlaylistTrack
from .forms import PlaylistForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from music.models import Track
from django.views.decorators.http import require_POST



# Create your views here.

@login_required
def playlist(request):
    playlists = Playlist.objects.filter(user=request.user)

    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        track_id = request.GET.get('track')

        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.user = request.user
            playlist.save()
            messages.success(request, 'Playlist successfully created')

            if track_id:
                url = reverse('playlist:playlist_list')
                return redirect(f'{url}?track={track_id}')

            return redirect('playlist:playlist_list')
        
    else:
        form = PlaylistForm()
        track_id = request.GET.get('track')

    return render(request, 'playlist/playlist_list.html', {'playlists':playlists, 'form':form,'track_id':track_id})


@login_required
def playlist_detail(request, pk):
    playlist = get_object_or_404(Playlist, pk=pk, user=request.user)
    return render(request, 'playlist/playlist_detail.html', {'playlist':playlist})

@login_required
@require_POST
def add_track_to_playlist(request, playlist_pk, track_pk):
    playlist = get_object_or_404(Playlist, pk=playlist_pk, user=request.user)

    track = get_object_or_404(Track, pk=track_pk)

    PlaylistTrack.objects.get_or_create(
        playlist=playlist,
        track=track
    )

    return redirect('playlist:playlist_detail', pk=playlist.pk)


@login_required
@require_POST
def remove_track_from_playlist(request, playlist_track_pk):
    playlist_track = get_object_or_404(PlaylistTrack, pk=playlist_track_pk, playlist__user=request.user)
    playlist_id = playlist_track.playlist_id

    playlist_track.delete()
        
    return redirect('playlist:playlist_detail', pk=playlist_id)


        
