# Generated by Django 5.0.6 on 2024-06-26 19:37
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("summarizer", "0002_alter_country_options_alter_lyrics_body_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Lyrics",
        ),
    ]
