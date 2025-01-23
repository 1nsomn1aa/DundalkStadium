from django.db import models
from django.contrib.auth.models import User

class GameType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Court(models.Model):
    name = models.CharField(max_length=100)
    game_type = models.ForeignKey(GameType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Booking(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)