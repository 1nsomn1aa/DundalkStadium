from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class News(models.Model):
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)

    def __str__(self):
        return self.title