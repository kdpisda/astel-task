from django.db import models

from utils.mixins.models.timestamp import TimeStampMixin


class Request(TimeStampMixin, models.Model):
    artist = models.CharField(max_length=255)
    song = models.CharField(max_length=255)
    lyrics = models.ForeignKey("Lyrics", on_delete=models.SET_NULL, null=True)
