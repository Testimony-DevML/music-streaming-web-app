from django.db import models

# Create your models here.
class Podcast(models.Model):
    title = models.CharField(max_length=200)
    host = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to='podcast_images/', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.host}'

class Episode(models.Model):
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, related_name='episodes')
    title = models.CharField(max_length=200)
    description = models.TextField()
    audio_file = models.FileField(upload_to='episode_audio/', blank=True)
    episode_number = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - EPISODE {self.episode_number}'
    
    
