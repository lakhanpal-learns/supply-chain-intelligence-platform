"""
Custom exceptions for ERPNext API client.
"""


class ERPNextError(Exception):
    """Base exception for all ERPNext client errors."""


class ERPNextAuthenticationError(ERPNextError):
    """Raised when authentication fails."""


class ERPNextConnectionError(ERPNextError):
    """Raised when connection to ERPNext fails."""


class ERPNextTimeoutError(ERPNextError):
    """Raised when request times out."""


class ERPNextAPIError(ERPNextError):
    """Raised when ERPNext returns an API error."""


class ERPNextResponseError(ERPNextError):
    """Raised when API response is invalid."""