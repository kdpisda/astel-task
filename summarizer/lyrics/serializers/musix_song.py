from rest_framework import serializers

from summarizer.lyrics.models.song import Song


class MusixSongSerializer(serializers.ModelSerializer):
    track_id = serializers.CharField(source="id", allow_null=False, allow_blank=False)
    track_name = serializers.CharField(
        source="name", allow_null=False, allow_blank=False
    )
    track_rating = serializers.CharField(
        source="rating", allow_null=False, allow_blank=False
    )
    explicit = serializers.CharField(
        source="explicit", allow_null=False, allow_blank=False
    )
    has_lyrics = serializers.CharField(
        source="has_lyrics", allow_null=False, allow_blank=False
    )
    has_subtitles = serializers.CharField(
        source="has_subtitles", allow_null=False, allow_blank=False
    )
    album_id = serializers.CharField(
        source="album_id", allow_null=False, allow_blank=False
    )
    album_name = serializers.CharField(
        source="album_name", allow_null=False, allow_blank=False
    )
    artist_id = serializers.CharField(
        source="artist_id", allow_null=False, allow_blank=False
    )
    artist_name = serializers.CharField(
        source="artist_name", allow_null=False, allow_blank=False
    )

    class Meta:
        model = Song
        fields = [
            "track_id",
            "track_name",
            "track_rating",
            "explicit",
            "has_lyrics",
            "has_subtitles",
            "album_id",
            "album_name",
            "artist_id",
            "artist_name",
        ]
