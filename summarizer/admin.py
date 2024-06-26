from django.contrib import admin

from summarizer.lyrics.admins.song import SongAdmin
from summarizer.lyrics.models.country import Country
from summarizer.lyrics.models.song import Song
from summarizer.requests.admins.request import RequestAdmin
from summarizer.requests.models.request import Request

# Register your models here.
admin.site.register(Song, SongAdmin)
admin.site.register(Country)
admin.site.register(Request, RequestAdmin)
