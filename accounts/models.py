from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    related_name='user_profile'
)
    profile_image = models.ImageField(upload_to='user_profile_image/', blank = True, null=True)

    def __str__(self):
        return self.user.username
