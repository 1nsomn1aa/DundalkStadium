from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from io import BytesIO


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    image = models.ImageField(default='default.png', upload_to='profile-pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)

                thumb_io = BytesIO()
                img.save(thumb_io, img.format)
                thumb_io.seek(0)
                file_name = self.image.name
                self.image.save(
                    file_name,
                    ContentFile(thumb_io.getvalue()),
                    save=False
                )

        super().save(*args, **kwargs)
