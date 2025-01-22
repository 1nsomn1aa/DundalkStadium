from django.db import models

class Sports(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Court(models.Model):
    name = models.CharField(max_length=100)
    sport_type = models.ForeignKey(Sports, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Bookings(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE, default=1)
    booking_time = models.DateTimeField()
    user_name = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name