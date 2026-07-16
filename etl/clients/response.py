from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class APIResponse:
    """
    Standard response object returned by the ERPNext API client.
    """

    success: bool
    status_code: int
    data: Any
    message: str | None = None