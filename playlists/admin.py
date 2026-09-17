from django.contrib import admin
from .models import Playlist, PlaylistTrack

# Register your models here.
admin.site.register(Playlist)
admin.site.register(PlaylistTrack)