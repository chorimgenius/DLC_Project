from django.db import models

class Review(models.Model):
    name = models.CharField(max_length = 20)
    content = models.TextField()
    rank = models.IntegerField()

