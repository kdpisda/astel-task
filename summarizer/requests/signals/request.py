import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from summarizer.requests.models.request import Request
from summarizer.requests.tasks.get_lyrics import get_lyrics


logger = logging.getLogger(__name__)


@receiver(post_save, sender=Request)
def process_request(sender, instance, created, **kwargs):
    if created:
        logger.info(f"Request ID: {instance.id} created initiating get_lyrics task")
        get_lyrics.delay(instance.id)
