from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Track(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=150)
    cover_image = models.ImageField(upload_to='track_images/', blank=True)
    audio_file = models.FileField(upload_to='track_audio/', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f'{self.title} - {self.artist}'

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.track}'

    class Meta:
        constraints = [models.UniqueConstraint(
            fields = ['user', 'track'], 
            name = 'unique_user_track_favorite'
        )]

class RecentlyPlayed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    last_played = models.DateTimeField(auto_now=True)
    position = models.FloatField(default=0)

    def __str__(self):
     return f'{self.track} - {self.last_played}'

    class Meta:
        constraints = [models.UniqueConstraint(
            fields = ['user', 'track'],
            name = 'unique_user_track_recentlyPlayed'
        )]
