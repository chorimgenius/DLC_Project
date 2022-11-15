from django.db import models
from user.models import User
#from user import models as user
#from musics import models as musics
from musics.models import Music

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_user') 
    music = models.ForeignKey(Music, on_delete=models.CASCADE, null=True, default='', related_name='review_set')
    content = models.TextField()
    rank = models.IntegerField()



    def __str__(self):
        return str(self.user)