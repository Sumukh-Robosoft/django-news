from django.db import models
from django.contrib.auth.models import AbstractUser, User


class User(AbstractUser):
    is_author = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)


class Articles(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='images/', blank=True)
    author = models.CharField(max_length = 100)
    publisher = models.CharField(max_length = 100)
    status = models.CharField(max_length=10)



    def __str__(self):
        return f"{self.title}"



