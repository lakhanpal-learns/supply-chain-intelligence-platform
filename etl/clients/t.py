from ..clients.erpnext_client import ERPNextClient

client = ERPNextClient()

print(client.health_check())

items = client.get_documents(
    "Item",
    {
        "limit_page_length": 5,
    },
)

from etl.config.settings import settings

print("API Key:", settings.erp.api_key)
print("Secret Length:", len(settings.erp.api_secret))
print("Secret Repr:", repr(settings.erp.api_secret))

print(items)



# python -m etl.clients.t.py
# python -m etl.config.test_config