from django.db import models

# Create your models here.
class Podcast(models.Model):
    title = models.CharField(max_length=200)
    host = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to='podcast_images/', blank=True)
    audio_file = models.FileField(upload_to='podcast_audio/', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.host}'

