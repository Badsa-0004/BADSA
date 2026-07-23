"""
Application startup logging.
"""

import logging

from core.constants import APP_NAME
from core.version import VERSION
from config import settings

logger = logging.getLogger("agent")


def log_startup() -> None:
    logger.info("=" * 60)
    logger.info("%s v%s starting...", APP_NAME, VERSION)
    logger.info("Voice: %s", settings.voice)
    logger.info("=" * 60)