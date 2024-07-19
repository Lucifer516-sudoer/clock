"""This module contains logging related things.
And Mainly an base logger that can be used to derive child loggers"""

import logging

from clock.backend.logger._custom_handler import (  # noqa: F401
    RichConsoleHandler,  # type: ignore
    RichFileHandler,  # type: ignore
)

app_logger: logging.Logger = logging.getLogger("clock")
flet_logger: logging.Logger = logging.getLogger("flet")
flet_core_logger: logging.Logger = logging.getLogger("flet_core")


def _configure_handler(logger: logging.Logger, handler: list[logging.Handler]):
    """Just removes any default handler to given logger and adds the given handlers to it.
    Never call this inside any script unless needed, bcoz removes all the already present logging handlers"""

    logger.handlers = []  # just makes the handler to be an none handler
    for hndlr in handler:
        if hndlr not in logger.handlers:
            logger.addHandler(hndlr)


def configure_present_loggers(
    loggers: list[logging.Logger] | None = None,
    handlers: list[logging.Handler] | None = None,
):
    """Just attaches the handlers to loggers"""
    if loggers:
        if handlers:
            for logger in loggers:
                _configure_handler(logger, handlers)
