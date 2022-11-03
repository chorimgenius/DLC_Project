from django.db import models

class Review(models.Model):
    ###
    user = models.ForeignKey(User, on_delte=models.CASCADE) #user를 쓸것인가? name을 쓸것인가
    name = models.CharField(max_length = 20)
    ###
    content = models.TextField()
    rank = models.IntegerField()

    def __str__(self):
        return str(self.user)
