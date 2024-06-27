from django.contrib import admin

from summarizer.logging.admins.gpt import GPTLogAdmin
from summarizer.logging.admins.musix import MusixLogAdmin
from summarizer.logging.models.gpt import GPTLog
from summarizer.logging.models.musix import MusixLog
from summarizer.lyrics.admins.song import SongAdmin
from summarizer.lyrics.models.country import Country
from summarizer.lyrics.models.song import Song
from summarizer.requests.admins.request import RequestAdmin
from summarizer.requests.models.request import Request

# Register your models here.
admin.site.register(Song, SongAdmin)
admin.site.register(Country)
admin.site.register(Request, RequestAdmin)
admin.site.register(MusixLog, MusixLogAdmin)
admin.site.register(GPTLog, GPTLogAdmin)
