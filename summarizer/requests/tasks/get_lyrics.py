import logging

from astel.celery import app
from summarizer.lyrics.models.country import Country
from summarizer.lyrics.models.song import Song
from summarizer.lyrics.models.song import SongStatus
from summarizer.lyrics.serializers.musix_song import MusixSongSerializer
from summarizer.requests.models.request import Request
from summarizer.requests.models.request import RequestStatus
from utils.external.musix import MusixMatchClient
from utils.external.openai import ChatGPTClient

logger = logging.getLogger("celery")


def update_request_status(req, status):
    req.status = status
    req.save()
    logger.info(f"Request ID: {req.id} status updated to {status}")


def update_song_status(song, status):
    song.status = status
    song.save()
    logger.info(f"Song ID: {song.id} status updated to {status}")


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


def bulk_create_countries(countries):
    countries_to_create = []
    for country in countries:
        countries_to_create.append(Country(name=country))
    return Country.objects.bulk_create(countries_to_create)


def upsert_countries(song, countries):
    existing_countries = Country.objects.filter(name__in=countries).values_list(
        "name", flat=True
    )
    countries_to_create = list(set(countries) - set(existing_countries))
    bulk_create_countries(countries_to_create)
    countries_to_map = Country.objects.filter(name__in=countries)
    song.countries.set(countries_to_map)
    update_song_status(song, SongStatus.COMPLETED)


def get_summary_and_countries(req, song):
    if not song:
        logger.info(f"Song not found for Request ID: {req.id}")
        return
    if not song.summary or song.status not in [SongStatus.COMPLETED, SongStatus.FAILED]:
        logger.info(f"Generating Summary for Request ID: {req.id}")
        gpt = ChatGPTClient()
        song.summary = gpt.get_song_summary(song.lyrics)
        update_song_status(song, SongStatus.SUMMARY_GENERATED)
        countries = gpt.get_countries(song.lyrics)
        upsert_countries(song, countries)


def get_track_and_lyrics(req):
    musix = MusixMatchClient()
    song = musix.get_track(req.artist, req.track)
    created_song = None
    if song:
        logger.info(f"Song Found: {song}")
        created_song = create_or_update_song(song)
        lyrics = musix.get_lyrics(req.artist, req.track)
        logger.info(f"Lyrics Found for request: {req.id}")
        if lyrics:
            created_song.lyrics = lyrics.get("lyrics", {}).get("lyrics_body", "")
            update_song_status(created_song, SongStatus.LYRICS_FETCHED)
            req.song = created_song
            update_request_status(req, RequestStatus.COMPLETED)
            get_summary_and_countries(req, created_song)
        else:
            update_request_status(req, RequestStatus.NOT_FOUND)
    else:
        update_request_status(req, RequestStatus.NOT_FOUND)
    return created_song


@app.task(queue="lyrics")
def get_lyrics(request_id):
    logger.info(f"Finding Lyrics for Request ID: {request_id}")
    try:
        if Request.objects.filter(
            id=request_id,
            status__in=[
                RequestStatus.INITIALIZED,
                RequestStatus.COMPLETED,
                RequestStatus.NOT_FOUND,
                RequestStatus.FAILED,
            ],
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
        logger.error(f"Error while processing Request ID: {request_id}")
        logger.error(err)
        if req:
            req.error = str(err)
            update_request_status(req, RequestStatus.FAILED)
