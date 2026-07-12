"""
constants.py

Application-wide constants for the
Supply Chain Intelligence Platform.

Only values that never change belong here.

Environment-specific values belong in settings.py.
"""

# ============================================================
# ERPNext
# ============================================================

API_VERSION = "/api/resource"

DEFAULT_HEADERS = {
    "Content-Type": "application/json"
}

# ============================================================
# ETL
# ============================================================

CHECKPOINT_FILENAME = "checkpoints.json"

JSON_FILE_EXTENSION = ".json"

# ============================================================
# Date & Time
# ============================================================

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

ISO_DATE_FORMAT = "%Y-%m-%d"

# ============================================================
# API
# ============================================================

DEFAULT_PAGE_SIZE = 500

# ============================================================
# Logging
# ============================================================

LOG_FILE_NAME = "etl.log"

ERROR_LOG_FILE_NAME = "error.log"

PIPELINE_LOG_FILE_NAME = "pipeline.log"

# ============================================================
# HTTP Status Codes
# ============================================================

HTTP_OK = 200

HTTP_CREATED = 201

HTTP_BAD_REQUEST = 400

HTTP_UNAUTHORIZED = 401

HTTP_FORBIDDEN = 403

HTTP_NOT_FOUND = 404

HTTP_INTERNAL_SERVER_ERROR = 500

