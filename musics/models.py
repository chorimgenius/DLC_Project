from django.db import models
from review.models import Review

# Create your models here.

class Music(models.Model):
    name = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    artists = models.CharField(max_length=50)
    likes = models.ManyToManyField(Review, related_name="like_music")
    image = models.models.ImageField()
