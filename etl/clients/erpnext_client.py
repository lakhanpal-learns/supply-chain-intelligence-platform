from __future__ import annotations

from .base_client import BaseClient
from ..config.settings import settings
from .response import APIResponse
from requests.exceptions import (
    ConnectionError,
    HTTPError,
    Timeout,
)

from .exceptions import (
    ERPNextAPIError,
    ERPNextAuthenticationError,
    ERPNextConnectionError,
    ERPNextResponseError,
    ERPNextTimeoutError,
)
class ERPNextClient(BaseClient):

    def __init__(self):

        super().__init__(
        base_url=str(settings.erp.base_url),
        timeout=settings.erp.timeout,
    )

        self.session.headers.update(
            {
                "Authorization": (
                    f"token "
                    f"{settings.erp.api_key.get_secret_value()}:"
                    f"{settings.erp.api_secret.get_secret_value()}"
                ),
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )

        # Temporary Debug
        # print(self.session.headers)

    # Health Check
    def health_check(self) -> bool:
        response = self.session.get(
            f"{self.base_url}/api/method/ping",
            timeout=self.timeout,
        )

        return response.ok
    
    # Generic GET Method
    # Everything should eventually go through one private method.
    
    def _get(
    self,
    endpoint: str,
    params: dict | None = None,
    ) -> APIResponse:

        try:

            response = self.session.get(
                f"{self.base_url}/api/{endpoint}",
                params=params,
                timeout=self.timeout,
            )

            response.raise_for_status()

            payload = response.json()

            return APIResponse(
                success=True,
                status_code=response.status_code,
                data=payload.get("data"),
                message=None,
            )

        except Timeout as exc:
            raise ERPNextTimeoutError(
                "Request timed out."
            ) from exc

        except ConnectionError as exc:
            raise ERPNextConnectionError(
                "Unable to connect to ERPNext."
            ) from exc

        except HTTPError as exc:

            if response.status_code == 401:
                raise ERPNextAuthenticationError(
                    "Invalid API credentials."
                ) from exc

            raise ERPNextAPIError(
                f"ERPNext returned HTTP {response.status_code}"
            ) from exc

        except ValueError as exc:
            raise ERPNextResponseError(
                "Invalid JSON response."
            ) from exc

    # Now every future method simply calls

    # return self._get(...)

    # instead of repeating HTTP logic.

    # Get Documents
    def get_documents(
    self,
    doctype: str,
    params: dict | None = None,
    ):

        endpoint = f"resource/{doctype}"

        return self._get(
            endpoint,
            params=params,
        )
    
    # Get Single Document
    def get_document(
    self,
    doctype: str,
    name: str,
    ):

        endpoint = f"resource/{doctype}/{name}"

        return self._get(endpoint)
    
    def get_all_documents(
    self,
    doctype: str,
    page_size: int = 500,
    ) -> APIResponse:
        """
        Retrieve all records for a DocType using ERPNext pagination.

        Args:
            doctype: ERPNext DocType name.
            page_size: Number of records per API request.

        Returns:
            APIResponse containing all records.
        """

        all_records = []
        offset = 0

        while True:

            response = self.get_documents(
                doctype=doctype,
                params={
                    "limit_start": offset,
                    "limit_page_length": page_size,
                },
            )

            records = response.data

            # No more records
            if not records:
                break

            # Add current page to final list
            all_records.extend(records)

            # Next page
            offset += page_size

        return APIResponse(
            success=True,
            status_code=200,
            data=all_records,
            message=f"Retrieved {len(all_records)} records.",
        )


# usage 
# client = ERPNextClient()

# print(client.health_check())

# # usage get document 

# client.get_documents("Item")


