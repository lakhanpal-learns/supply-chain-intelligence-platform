from __future__ import annotations

import requests
from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class BaseClient:
    """
    Base HTTP client.

    Responsibilities:
    - HTTP session management
    - Connection pooling
    - Retry strategy
    - Request timeout
    """

    def __init__(
        self,
        base_url: str,
        timeout: int = 30,
    ) -> None:

        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

        # Create reusable HTTP session
        self.session: Session = requests.Session()

        # Configure retry strategy
        retry_strategy = Retry(
            total=3,
            connect=3,
            read=3,
            backoff_factor=5,
            status_forcelist=[
                429,  # Too Many Requests
                500,  # Internal Server Error
                502,  # Bad Gateway
                503,  # Service Unavailable
                504,  # Gateway Timeout
            ],
            allowed_methods={"GET"},
            raise_on_status=False,
        )

        # Mount retry adapter
        adapter = HTTPAdapter(max_retries=retry_strategy)

        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def close(self) -> None:
        """Close the HTTP session."""
        self.session.close()

    
# One improvement

# The retry configuration is currently hardcoded.

# A more scalable approach is to move these values into your configuration so they can be changed without editing code.

# For example, in settings.py:

# retry_attempts: int = 3
# retry_backoff_factor: int = 5

# Then in BaseClient:

# Retry(
#     total=settings.erp.retry_attempts,
#     backoff_factor=settings.erp.retry_backoff_factor,
#     ...
# )

# This makes the retry behavior configurable for development, testing, and production.