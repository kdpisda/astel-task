import logging

from astel.celery import app
from summarizer.lyrics.models.song import Song
from summarizer.lyrics.serializers.musix_song import MusixSongSerializer
from summarizer.requests.models.request import Request
from summarizer.requests.models.request import RequestStatus
from utils.external.musix import MusixMatchClient

logger = logging.getLogger("celery")


def update_request_status(req, status):
    req.status = status
    req.save()


def create_or_update_song(song_body):
    song_body = song_body["track"]
    song_id = song_body["track_id"]
    song = None
    if Song.objects.filter(id=song_id).exists():
        song = Song.objects.get(id=song_id)
    if song:
        serializer = MusixSongSerializer(song, data=song_body)
    else:
        serializer = MusixSongSerializer(data=song_body)
    serializer.is_valid(raise_exception=True)
    return serializer.save()


def get_track_and_lyrics(req):
    musix = MusixMatchClient()
    song = musix.get_track(req.artist, req.track)
    if song:
        created_song = create_or_update_song(song)
        lyrics = musix.get_lyrics(req.artist, req.track)
        if lyrics:
            created_song.lyrics = lyrics.get("lyrics", {}).get("lyrics_body", "")
            created_song.save()
            req.song = created_song
            update_request_status(req, RequestStatus.FOUND)
        else:
            update_request_status(req, RequestStatus.NOT_FOUND)
    else:
        update_request_status(req, RequestStatus.NOT_FOUND)


@app.task(queue="lyrics")
def get_lyrics(request_id):
    logger.info(f"Finding Lyrics for Request ID: {request_id}")
    try:
        if Request.objects.filter(
            id=request_id, status=RequestStatus.INITIALIZED
        ).exists():
            req = Request.objects.get(id=request_id)
            req.errors = None
            update_request_status(req, RequestStatus.PROCESSING)
            get_track_and_lyrics(req)
        else:
            logger.info(
                f"Request ID: {request_id} not found or already processing/processed."
            )
    except Exception as err:
        if req:
            req.error = str(err)
            update_request_status(req, RequestStatus.FAILED)
