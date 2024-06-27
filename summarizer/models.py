from auditlog.registry import auditlog

from summarizer.logging.models.musix import MusixLog
from summarizer.logging.models.openai import GPTLog
from summarizer.lyrics.models.country import Country
from summarizer.lyrics.models.song import Song
from summarizer.requests.models.request import Request

auditlog.register(Song)
auditlog.register(Country)
auditlog.register(Request)
auditlog.register(MusixLog)
auditlog.register(GPTLog)
