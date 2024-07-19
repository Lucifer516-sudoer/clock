"""
Module: custom_handler

This module provides custom handler implementations for console and file logging
using the rich library for formatted output.

The module defines two functions:

1. RichConsoleHandler: Creates a RichHandler instance for console logging.
2. RichFileHandler: Creates a RichHandler instance for file logging.

These handlers can be used with the standard Python logging module to log messages
with rich formatting and custom log time format.

Example usage:
    ```python
    import logging
    from pathlib import Path
    from custom_handler import RichConsoleHandler, RichFileHandler

    logger = logging.getLogger(__name__)

    console_handler = RichConsoleHandler(level=logging.DEBUG)
    file_handler = RichFileHandler(level=logging.INFO, file=Path("app.log"))

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    ```
"""

import logging
from pathlib import Path

from rich.console import Console
from rich.logging import RichHandler


def RichConsoleHandler(level: int | str = logging.NOTSET) -> RichHandler:
    """
    Create a RichHandler instance for console logging.

    Args:
        level (int | str, optional): The logging level. Defaults to logging.NOTSET.

    Returns:
        RichHandler: A RichHandler instance for console logging.
    """
    return RichHandler(
        level=level,
        console=Console(file=None),
        rich_tracebacks=True,
        log_time_format="[%I:%M:%S %p %d/%m/%Y]",
    )


def RichFileHandler(
    level: int | str = logging.NOTSET, file: Path = Path("log.log")
) -> RichHandler:
    """
    Create a RichHandler instance for file logging.

    Args:
        level (int | str, optional): The logging level. Defaults to logging.NOTSET.
        file (Path, optional): The file path to log to. Defaults to Path("log.log").

    Returns:
        RichHandler: A RichHandler instance for file logging.
    """
    file_console = Console(file=open(file, "a+", encoding="utf-8"), width=115)
    return RichHandler(
        level=level,
        console=file_console,
        rich_tracebacks=True,
        log_time_format="[%I:%M:%S %p %d/%m/%Y]",
    )
