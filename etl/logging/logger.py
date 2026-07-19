from __future__ import annotations

import logging
from pathlib import Path

# -----------------------------------------------------
# Create logs directory
# -----------------------------------------------------

LOG_DIR = Path("etl/logging/logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "etl.log"

# -----------------------------------------------------
# Create logger
# -----------------------------------------------------

logger = logging.getLogger("etl")

logger.setLevel(logging.INFO)

# Prevent duplicate logs
logger.propagate = False

# -----------------------------------------------------
# Formatter
# -----------------------------------------------------

formatter = logging.Formatter(
    fmt="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# -----------------------------------------------------
# File Handler
# -----------------------------------------------------

file_handler = logging.FileHandler(LOG_FILE)

file_handler.setFormatter(formatter)

# -----------------------------------------------------
# Console Handler
# -----------------------------------------------------

console_handler = logging.StreamHandler()

console_handler.setFormatter(formatter)

# -----------------------------------------------------
# Avoid duplicate handlers
# -----------------------------------------------------

if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)