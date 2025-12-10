import logging
from pathlib import Path
from typing import Optional


def ensure_dir(path: str) -> None:
    """Create a directory if it does not exist."""
    Path(path).mkdir(parents=True, exist_ok=True)


def setup_logger(log_file: Optional[str] = None) -> logging.Logger:
    """Set up a simple logger for the project."""
    logger = logging.getLogger("schema_validator")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"
        )
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.INFO)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

    return logger
