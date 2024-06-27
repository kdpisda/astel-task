import logging

from django.apps import AppConfig

logger = logging.getLogger(__name__)


class SummarizerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "summarizer"

    def ready(self):
        from summarizer.requests.signals.request import process_request  # noqa

        logger.info("Imported Signals")
