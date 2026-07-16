from __future__ import annotations

from .base_client import BaseClient
from ..config.settings import settings


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
        print(self.session.headers)

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
    ):

        response = self.session.get(
            f"{self.base_url}/api/{endpoint}",
            params=params,
            timeout=self.timeout,
        )
        
        # tempeory dubug 
        print("=" * 50)
        print("Status Code :", response.status_code)
        print("Response Body:")
        print(response.text)
        print("=" * 50)

        if response.status_code != 200:
            print("Status:", response.status_code)
            print("Body:", response.text)
            return None

        return response.json()

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
    


# usage 
# client = ERPNextClient()

# print(client.health_check())

# # usage get document 

# client.get_documents("Item")


