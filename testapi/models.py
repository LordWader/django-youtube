from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class KeyWordData(models.Model):
    key_word = models.CharField(max_length=100)
    videos = models.ManyToManyField('YouTubeVideo')

    class Meta:
        ordering = ("key_word",)

    def __str__(self):
        return self.key_word


class YouTubeVideo(models.Model):
    url = models.CharField(max_length=10000)

    class Meta:
        ordering = ("url",)

    def __str__(self):
        return f"{self.url}"


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
