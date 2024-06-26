from django.contrib import admin


class SongAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "artist_id",
        "artist_name",
        "rating",
        "explicit",
        "has_lyrics",
        "album_id",
        "album_name",
    )
    list_filter = ("explicit", "has_lyrics")
    search_fields = ("name", "artist_name", "album_name")
