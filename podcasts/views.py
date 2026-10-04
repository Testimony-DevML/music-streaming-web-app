from django.shortcuts import render
from .models import Podcast, Episode
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required
def podcast_list(request):
    podcasts = Podcast.objects.all()

    category = request.GET.get('genre', 'All')
    if category != 'All':
        podcasts = podcasts.filter(category__iexact=category)

    return render(request, 'podcasts/podcast_list.html', {'podcasts':podcasts, 'genre':category})

def podcast_detail(request, pk):
    podcast = get_object_or_404(Podcast, pk=pk)

    return render(request, 'podcasts/podcast_detail.html', {'podcast':podcast})

