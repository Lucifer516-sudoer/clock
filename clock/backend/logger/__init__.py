"""This module contains logging related things.
And Mainly an base logger that can be used to derive child loggers"""

import logging
from typing import TypeAlias

from clock.backend.logger.logger import (
    RichConsoleHandler,
    RichFileHandler,
    app_logger,
    configure_present_loggers,
    flet_core_logger,
    flet_logger,
)

Logger: TypeAlias = logging.Logger
__all__ = [
    "Logger",
    "app_logger",
    "RichConsoleHandler",
    "RichFileHandler",
    "configure_present_loggers",
    "logging",
    "flet_logger",
    "flet_core_logger",
]
