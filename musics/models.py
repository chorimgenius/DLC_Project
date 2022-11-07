from django.db import models
from user.models import User

# Create your models here.

class Music(models.Model):
    name = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    artists = models.CharField(max_length=50)
    album = models.TextField()
    likes = models.ManyToManyField(User, related_name="likes_music")
    music_image = models.ImageField(default='', max_length=255, null=True)
    
    def __str__(self):
        return str(self.name)
