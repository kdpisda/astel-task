from auditlog.registry import auditlog

from summarizer.lyrics.models.country import Country
from summarizer.lyrics.models.song import Song

auditlog.register(Song)
auditlog.register(Country)
