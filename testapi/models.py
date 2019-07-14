from django.db import models, connection


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
        ordering = ("url", )

    def __str__(self):
        return f"{self.url}"
