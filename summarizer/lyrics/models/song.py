from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models

from utils.mixins.models.timestamp import TimeStampMixin


class Song(TimeStampMixin, models.Model):
    name = models.CharField(max_length=255, help_text="Name of the song.")
    artist_id = models.IntegerField(help_text="ID of the artist.")
    artist_name = models.CharField(max_length=255, help_text="Name of the artist.")
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        help_text="Rating of the song. 0-5 scale.",
    )
    explicit = models.BooleanField(
        default=False, help_text="Indicates whether the song is explicit."
    )
    has_lyrics = models.BooleanField(
        default=False, help_text="Indicates whether the song has lyrics."
    )
    lyrics = models.TextField(help_text="Lyrics of the song.")
    has_subtitles = models.BooleanField(
        default=False, help_text="Indicates whether the song has subtitles."
    )
    album_id = models.IntegerField(help_text="ID of the album.")
    album_name = models.CharField(max_length=255, help_text="Name of the album.")

    countries = models.ManyToManyField(
        "Country", related_name="songs", help_text="Countries found in the song."
    )
