import logging

from rich.logging import RichHandler


def setup_logger() -> logging.Logger:
    """
    Configure and return the application logger.
    """

    logger = logging.getLogger("knowledgeforge")

    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    handler = RichHandler(
        rich_tracebacks=True,
        show_path=False,
        markup=True,
    )

    formatter = logging.Formatter(
        "%(message)s"
    )

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    logger.propagate = False

    return logger


logger = setup_logger()