from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)


class Commentary(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='commentary')
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='commentary')
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
