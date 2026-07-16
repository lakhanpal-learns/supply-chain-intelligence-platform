from __future__ import annotations

from .base_client import BaseClient
from config.settings import settings


class ERPNextClient(BaseClient):

    def __init__(self):

        super().__init__(
            base_url=settings.erp.base_url,
            timeout=settings.erp.timeout,
        )

        self.session.headers.update(
            {
                "Authorization": (
                    f"token "
                    f"{settings.erp.api_key}:"
                    f"{settings.erp.api_secret}"
                ),
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )
    # Health Check
    def health_check(self) -> bool:

        response = self.session.get(
            f"{self.base_url}/method/ping",
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
            f"{self.base_url}/{endpoint}",
            params=params,
            timeout=self.timeout,
        )

        response.raise_for_status()

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
client = ERPNextClient()

print(client.health_check())

# usage get document 

client.get_documents("Item")


