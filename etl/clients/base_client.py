from __future__ import annotations

import requests
from requests import Session


class BaseClient:
    """
    Base HTTP client.

    Handles:

    - Session management
    - Common headers
    - Timeouts
    """

    def __init__(
        self,
        base_url: str,
        timeout: int = 30,
    ) -> None:

        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

        self.session: Session = requests.Session()

    def close(self) -> None:
        """Close HTTP session."""

        self.session.close()