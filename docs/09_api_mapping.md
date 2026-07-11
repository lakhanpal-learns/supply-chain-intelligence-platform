# API Mapping

## Project

Supply Chain Intelligence Platform

---

# Document Information

| Field | Value |
|-------|-------|
| Document Type | API Mapping |
| Version | 1.0 |
| Status | final |
| Project | Supply Chain Intelligence Platform |
| Prepared By | Lakhanpal |
| Last Updated | July 2026 |

---

# Purpose

The purpose of this document is to define every ERPNext REST API endpoint required by the Supply Chain Intelligence Platform.

For each business entity, this document specifies:

- REST API endpoint
- HTTP method
- Authentication
- Query parameters
- Pagination strategy
- Incremental extraction field
- Response format
- Target Bronze table

This document serves as the implementation guide for the ETL pipeline developed during Phase 3.

---

# API Overview

The ETL pipeline communicates with ERPNext exclusively through the official REST API.

```text
Python ETL
      │
Token Authentication
      │
HTTPS Request
      │
ERPNext REST API
      │
JSON Response
      │
Bronze Layer
      │
Silver Layer
      │
Gold Layer
```

No direct SQL queries will be executed against the ERPNext MariaDB database.

---

# Base URL

For the local development environment:

```
http://globalmart.localhost:8080/api/resource/
```

Every business entity is accessed by appending its DocType to the base URL.

Example:

```
http://localhost:8000/api/resource/Item
```

---

# Authentication

All API requests require authentication.

Version 1 uses ERPNext API Key and API Secret generated from the Administrator user account. Credentials are stored securely using environment variables.

Authentication Header

```
Authorization: token API_KEY:API_SECRET
```

API credentials will be stored securely using environment variables.

---

# Common Query Parameters

| Parameter | Purpose |
|-----------|---------|
| fields | Select required columns |
| filters | Filter records |
| limit_page_length | Number of records returned |
| limit_start | Pagination offset |
| order_by | Sort records |
| as_dict | Return JSON objects |

---

# Standard Response Format

ERPNext returns JSON responses.

Example

```json
{
  "data": [
    {
      "name": "ITEM-0001",
      "item_name": "Laptop",
      "modified": "2026-07-10 09:30:00"
    }
  ]
}
```

---

# API Mapping

| DocType               | Endpoint                            | Method | Incremental Field | Primary Key | Target Bronze Table          |
| --------------------- | ----------------------------------- | ------ | ----------------- | ----------- | ---------------------------- |
| Item Group            | /api/resource/Item Group            | GET    | modified          | name        | bronze_item_group            |
| UOM                   | /api/resource/UOM                   | GET    | modified          | name        | bronze_uom                   |
| Purchase Order Item   | /api/resource/Purchase Order Item   | GET    | modified          | name        | bronze_purchase_order_item   |
| Purchase Receipt Item | /api/resource/Purchase Receipt Item | GET    | modified          | name        | bronze_purchase_receipt_item |
| Purchase Invoice      | /api/resource/Purchase Invoice      | GET    | modified          | name        | bronze_purchase_invoice      |
| Purchase Invoice Item | /api/resource/Purchase Invoice Item | GET    | modified          | name        | bronze_purchase_invoice_item |
| Sales Invoice         | /api/resource/Sales Invoice         | GET    | modified          | name        | bronze_sales_invoice         |
| Sales Invoice Item    | /api/resource/Sales Invoice Item    | GET    | modified          | name        | bronze_sales_invoice_item    |
| Stock Entry Detail    | /api/resource/Stock Entry Detail    | GET    | modified          | name        | bronze_stock_entry_detail    |
| Stock Ledger Entry    | /api/resource/Stock Ledger Entry    | GET    | modified          | name        | bronze_stock_ledger_entry    |


---

# Incremental Extraction

All transactional and master tables contain the **modified** timestamp. The modified field was validated across all selected ERPNext DocTypes during Phase 2.

The ETL pipeline will request only records modified after the previous successful extraction.

Example filter

```
filters=[
    ["modified", ">", "2026-07-09 00:00:00"]
]
```

This minimizes network traffic and extraction time.

---

# Pagination Strategy

Large datasets require pagination.

Standard configuration

| Parameter | Value |
|-----------|------|
| limit_page_length | 500 |
| limit_start | 0, 500, 1000 ... |

The ETL pipeline will continue requesting pages until no additional records are returned.

---

# Selected Fields

To reduce payload size, only required fields will be extracted. Field selection is based on the validated ERPNext schema and will be customized for each DocType.

Example

```
fields=[
    "name",
    "item_code",
    "item_name",
    "modified"
]
```

Field selection will be customized for each DocType.

---

# Error Handling

The ETL pipeline must handle the following scenarios.

| Error | Action |
|--------|--------|
| Authentication Failure | Stop pipeline |
| Network Timeout | Retry |
| Server Error | Retry with backoff |
| Empty Response | Continue |
| Invalid JSON | Log and fail |

---

# Retry Policy

| Attempt | Delay |
|----------|-------|
| First Retry | 5 seconds |
| Second Retry | 15 seconds |
| Third Retry | 30 seconds |

After three unsuccessful attempts, the extraction will be marked as failed.

---

# Logging Requirements

Each API request should capture:

- Extraction timestamp
- Endpoint
- Execution time
- HTTP status
- Records extracted
- Retry count
- Success or failure
- API endpoint
- DocType
- Records skipped
- Records failed

These logs will support monitoring and troubleshooting.

---

# Security Considerations

The ETL application will:

- Never hardcode API credentials.
- Store secrets in environment variables.
- Use HTTPS in production environments.
- Restrict API permissions to read-only access.
- Prevent sensitive information from appearing in logs.

---

# Phase 3 Implementation Impact

This document directly defines:

- Python API client
- Authentication module
- Endpoint configuration
- Incremental loading logic
- Pagination implementation
- Bronze layer loading

Every API call developed during Phase 3 will follow this specification.

---

# Key Takeaways

- ERPNext REST API is the exclusive data extraction interface.
- Every selected DocType has a dedicated API endpoint.
- Incremental extraction uses the **modified** timestamp.
- Pagination supports large datasets.
- API credentials remain external to the application.
- Logging and retry policies improve reliability.

---

# Next Document

The next document is **10_data_extraction_strategy.md**, which defines the complete ETL extraction methodology, including full loads, incremental loads, execution sequence, scheduling, error recovery, logging, and operational best practices.