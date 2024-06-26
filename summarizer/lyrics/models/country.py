from django.db import models

from utils.mixins.models.timestamp import TimeStampMixin


class Country(TimeStampMixin, models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Countries"
        verbose_name = "Country"
