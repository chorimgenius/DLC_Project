from django.db import models
from user.models import User
from musics.models import Music

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    music = models.ForeignKey(Music, on_delete=models.CASCADE, null=True, default='')
    content = models.TextField()
    rank = models.IntegerField()



    def __str__(self):
        return str(self.user)