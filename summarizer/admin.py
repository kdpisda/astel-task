from django.contrib import admin

from summarizer.lyrics.models.country import Country
from summarizer.lyrics.models.song import Song

# Register your models here.
admin.site.register(Song)
admin.site.register(Country)
