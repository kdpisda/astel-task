# Generated by Django 5.0.6 on 2024-06-27 13:25
from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("summarizer", "0009_gptlog_musixlog"),
    ]

    operations = [
        TrigramExtension(),
    ]
