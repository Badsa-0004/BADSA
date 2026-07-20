"""
Application startup logging.
"""

import logging

from core.constants import APP_NAME
from core.version import VERSION

logger = logging.getLogger("agent")


def log_startup() -> None:
    """Log application startup information."""
    logger.info("=" * 60)
    logger.info("%s v%s starting...", APP_NAME, VERSION)
    logger.info("=" * 60)