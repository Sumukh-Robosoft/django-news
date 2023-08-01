from django.db import models
from django.contrib.auth.models import AbstractUser, User


class User(AbstractUser):
    is_author = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)


class Articles(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to=None)
    author = models.ForeignKey(User, related_name="author", on_delete=models.CASCADE)
    publisher = models.ForeignKey(
        User, related_name="publisher", on_delete=models.CASCADE, null=True
    )
    status = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.title}"
