from django.db import models

from utils.mixins.models.timestamp import TimeStampMixin


class RequestStatus(models.TextChoices):
    PROCESSING = "PROCESSING", "Processing"
    FOUND = "FOUND", "Found"
    NOT_FOUND = "NOT_FOUND", "Not Found"
    FAILED = "FAILED", "Failed"


class Request(TimeStampMixin, models.Model):
    artist = models.CharField(max_length=255, help_text="Name of the artist.")
    track = models.CharField(max_length=255, help_text="Name of the track.")
    song = models.ForeignKey(
        "Song", on_delete=models.SET_NULL, null=True, help_text="Reference to the song."
    )
    status = models.CharField(
        choices=RequestStatus.choices,
        default=RequestStatus.PROCESSING,
        max_length=255,
        help_text="Status of the request.",
    )
