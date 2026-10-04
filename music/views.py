from django.shortcuts import render, get_object_or_404
from .models import Track
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Track, RecentlyPlayed, Favorite
from django.http import JsonResponse
import json
from django.db.models import Q

# Create your views here.
@login_required
def music_list(request):
    tracks = Track.objects.all() 

    genre = request.GET.get('genre', 'All')
    if genre != 'All':
        tracks = tracks.filter(genre__iexact=genre)

    return render(request, 'music/music_list.html', {'tracks': tracks, 'genre':genre})

@login_required
@require_POST
def recently_played(request, track_pk):
    track = get_object_or_404(Track, pk=track_pk)
    recently_played, created = RecentlyPlayed.objects.get_or_create(
        user = request.user,
        track = track
    )

    return JsonResponse(
            {
            'success': True,
            'created' : created
            }
        )

@login_required
@require_POST 
def saved_position(request, track_pk):
    data = json.loads(request.body)
    position = data.get('position')

    if position is None:
        return JsonResponse(
            {
                'success': False,
                'error': 'Position was not provided'
            },
            status = 400
        )

    recently_played = get_object_or_404(RecentlyPlayed, user=request.user, track_id=track_pk)
    recently_played.position = position
    recently_played.save()

    return JsonResponse(
        {
            'success': True,
            'position': recently_played.position
        }
    )

# def resume_position(request, track_pk):
#     recently_played = RecentlyPlayed.objects.filter(user=request.user, track_id=track_pk).first()
#     if recently_played:
#         position = recently_played.position
#     else:
#         position = 0

#     return JsonResponse({
#         'position': position
#     })

@login_required
def recently_played_list(request):
    recently_played = RecentlyPlayed.objects.filter(user=request.user).order_by('-last_played')

    return render(request, 'music/recently_played_list.html', {'recently_played': recently_played})


@login_required
@require_POST
def toggle_favorite(request, track_pk):
    favorite = Favorite.objects.filter(user=request.user, track_id=track_pk).first()

    if(favorite):
        favorite.delete()
        favorited = False

    else:
        Favorite.objects.create(user=request.user, track_id=track_pk)
        favorited = True

    return JsonResponse({
        'success':True,
        'favorited':favorited
    })


@login_required
def favorite_list(request):
    favorites = Favorite.objects.filter(user=request.user)

    return render(request, 'music/favorite_list.html', {'favorites': favorites})


@login_required
def search(request):

    query = request.GET.get('q', '').strip()

    tracks = Track.objects.none()

    if query:
        tracks = Track.objects.filter(
            Q(title__icontains=query) |
            Q(artist__icontains=query) |
            Q(genre__icontains=query)
        )

    return render(
        request,
        'music/search_results.html',
        {
            'query': query,
            'tracks': tracks
        }
    )
