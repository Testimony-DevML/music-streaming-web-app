from django.contrib import admin
from .models import Track, Favorite, RecentlyPlayed

# Register your models here.
admin.site.register(Track)
admin.site.register(Favorite)
admin.site.register(RecentlyPlayed)
