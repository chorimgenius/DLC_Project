from django.db import models
from user.models import User

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    content = models.TextField()
    rank = models.IntegerField()

    def __str__(self):
        return str(self.user)
