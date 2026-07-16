from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class APIResponse:
    success: bool
    status_code: int
    data: Any
    message: str | None = None