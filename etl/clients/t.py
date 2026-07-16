from ..clients.erpnext_client import ERPNextClient
from .exceptions import ERPNextError

client = ERPNextClient()

try:
    print(client.health_check())

    items = client.get_documents(
        "Item",
        {
            "limit_page_length": 5,
        },
    )

    response = client.get_all_documents("Item")

    print(type(response))
    print(response.success)
    print(response.status_code)

    if response.success:
        print(response.data)

    print(items)

except ERPNextError as exc:
    print(exc)
    
# python -m etl.clients.t
# python -m etl.config.test_config