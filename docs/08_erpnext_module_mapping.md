# ERPNext Module Mapping

## Project

Supply Chain Intelligence Platform

---

# Document Information

| Field | Value |
|-------|-------|
| Document Type | ERPNext Module Mapping |
| Version | 1.0 |
| Status | final |
| Project | Supply Chain Intelligence Platform |
| Prepared By | Lakhanpal |
| Last Updated | July 2026 |

---

# Purpose

The purpose of this document is to identify the ERPNext modules and DocTypes required for the Supply Chain Intelligence Platform.

Each business process defined during Phase 1 is mapped to the corresponding ERPNext DocTypes that store operational data.

This mapping defines the scope of the ETL pipeline and serves as the foundation for API extraction, Bronze layer design, source-to-target mapping, and dimensional modeling.

---

# Business Process Overview

The analytics platform covers the complete supply chain lifecycle.

```text
Supplier
      │
      ▼
Purchase Requisition
      │
      ▼
Purchase Order
      │
      ▼
Purchase Order Item
      │
      ▼
Purchase Receipt
      │
      ▼
Purchase Receipt Item
      │
      ▼
  Warehouse
      │
      ▼
Stock Movement
      │
      ▼
Sales Order
      │
      ▼
Delivery Note
      │
      ▼
Sales Invoice
      │
      ▼
Sales Invoice Item
      │
      ▼
Customer
      │
      ▼
Returns
```

---

# ERPNext Module Mapping

| Business Process       | ERP Module | ERPNext DocType       | Priority | Incremental Field | Target Bronze Table          |
| ---------------------- | ---------- | --------------------- | -------- | ----------------- | ---------------------------- |
| Purchase Order Lines   | Buying     | Purchase Order Item   | High     | modified          | bronze_purchase_order_item   |
| Purchase Receipt Lines | Buying     | Purchase Receipt Item | High     | modified          | bronze_purchase_receipt_item |
| Purchase Invoice       | Buying     | Purchase Invoice      | Medium   | modified          | bronze_purchase_invoice      |
| Purchase Invoice Lines | Buying     | Purchase Invoice Item | Medium   | modified          | bronze_purchase_invoice_item |
| Sales Invoice          | Selling    | Sales Invoice         | Medium   | modified          | bronze_sales_invoice         |
| Sales Invoice Lines    | Selling    | Sales Invoice Item    | Medium   | modified          | bronze_sales_invoice_item    |
| Stock Movement Details | Stock      | Stock Entry Detail    | High     | modified          | bronze_stock_entry_detail    |
| Inventory Ledger       | Stock      | Stock Ledger Entry    | High     | modified          | bronze_stock_ledger_entry    |


---

# Extraction Priority

## High Priority

These entities are required for Version 1.

| DocType | Reason |
|----------|--------|
| Supplier | Procurement analytics |
| Item | Product analytics |
| Warehouse | Warehouse analytics |
| Bin | Inventory KPIs |
| Purchase Order | Procurement KPIs |
| Purchase Receipt | Lead Time calculations |
| Stock Entry | Inventory movement |
| Customer | Customer analytics |
| Sales Order | Sales KPIs |
| Delivery Note | Logistics KPIs |

---

## Medium Priority

These entities improve analytical capabilities but are not mandatory for the first ETL implementation.

| DocType | Reason |
|----------|--------|
| Material Request | Procurement planning |
| Sales Invoice | Revenue analysis |
| Purchase Invoice | Procurement cost analysis |

---

## Out of Scope (Version 1)

The following ERP modules are intentionally excluded.

| Module | Reason |
|----------|--------|
| Manufacturing | Outside project scope |
| Projects | Not required |
| HR | Not related to supply chain |
| CRM | Future enhancement |
| Quality | Future enhancement |
| Assets | Future enhancement |

---

# Module Relationships

```text
Supplier
      │
      ▼
Purchase Order
      │
      ▼
Purchase Receipt
      │
      ▼
Warehouse
      │
      ▼
Bin
      │
      ▼
Stock Entry

Customer
      │
      ▼
Sales Order
      │
      ▼
Delivery Note


Purchase Order
      │
      ▼
Purchase Order Item

Purchase Receipt
      │
      ▼
Purchase Receipt Item

Sales Invoice
      │
      ▼
Sales Invoice Item

Stock Entry
      │
      ▼
Stock Entry Detail

```

These relationships define the order in which data should be extracted and later transformed.

---

# Data Dependencies

Certain DocTypes depend on others.

| Parent Entity    | Child Entity          | Dependency                                                     |
| ---------------- | --------------------- | -------------------------------------------------------------- |
| Supplier         | Purchase Order        | Supplier must exist before Purchase Orders are extracted.      |
| Customer         | Sales Order           | Customer must exist before Sales Orders are extracted.         |
| Item             | Purchase Order Item   | Item must exist before Purchase Order Items are extracted.     |
| Item             | Purchase Receipt Item | Item must exist before Purchase Receipt Items are extracted.   |
| Item             | Purchase Invoice Item | Item must exist before Purchase Invoice Items are extracted.   |
| Item             | Sales Invoice Item    | Item must exist before Sales Invoice Items are extracted.      |
| Item             | Stock Entry Detail    | Item must exist before Stock Entry Details are extracted.      |
| Warehouse        | Bin                   | Warehouse must exist before inventory snapshots are extracted. |
| Item             | Bin                   | Item must exist before inventory snapshots are extracted.      |
| Purchase Order   | Purchase Order Item   | Parent Purchase Order must exist before its line items.        |
| Purchase Order   | Purchase Receipt      | Purchase Receipt references a Purchase Order.                  |
| Purchase Receipt | Purchase Receipt Item | Parent Purchase Receipt must exist before its line items.      |
| Purchase Invoice | Purchase Invoice Item | Parent Purchase Invoice must exist before its line items.      |
| Sales Order      | Delivery Note         | Delivery Note references a Sales Order.                        |
| Sales Invoice    | Sales Invoice Item    | Parent Sales Invoice must exist before its line items.         |
| Stock Entry      | Stock Entry Detail    | Parent Stock Entry must exist before its detail records.       |


These dependencies will determine the ETL extraction sequence.

---

# Recommended Extraction Order

The ETL pipeline should extract data in the following order.

| Step | DocType               | Reason                        |
| ---- | --------------------- | ----------------------------- |
| 1    | Supplier              | Master Data                   |
| 2    | Customer              | Master Data                   |
| 3    | Item                  | Master Data                   |
| 4    | Warehouse             | Master Data                   |
| 5    | Item Group            | Master Data Classification    |
| 6    | UOM                   | Measurement Reference Data    |
| 7    | Bin                   | Inventory Snapshot            |
| 8    | Material Request      | Procurement Planning          |
| 9    | Purchase Order        | Procurement Transactions      |
| 10   | Purchase Order Item   | Purchase Order Line Items     |
| 11   | Purchase Receipt      | Goods Receipt                 |
| 12   | Purchase Receipt Item | Goods Receipt Line Items      |
| 13   | Purchase Invoice      | Procurement Cost Transactions |
| 14   | Purchase Invoice Item | Purchase Invoice Line Items   |
| 15   | Stock Entry           | Inventory Movement            |
| 16   | Stock Entry Detail    | Inventory Movement Line Items |
| 17   | Stock Ledger Entry    | Inventory Transaction History |
| 18   | Sales Order           | Sales Transactions            |
| 19   | Delivery Note         | Order Fulfillment             |
| 20   | Sales Invoice         | Sales Billing                 |
| 21   | Sales Invoice Item    | Sales Invoice Line Items      |


Master data is extracted before transactional data to maintain referential integrity.

---

# Business KPIs Supported

| DocType | Supported KPIs |
|----------|----------------|
| Supplier | Supplier Performance, Supplier Spend, Lead Time |
| Item | Inventory Value, ABC Classification |
| Warehouse | Warehouse Utilization |
| Bin | Inventory Level, Stockout Rate |
| Purchase Order | Purchase Cycle Time |
| Purchase Receipt | Supplier Lead Time |
| Stock Entry | Stock Movement |
| Sales Order | Order Fulfillment Rate |
| Delivery Note | On-Time Delivery, Perfect Order Rate |
| Customer | Customer Order Analysis |

---

# Design Decisions

The following decisions were made during module selection.

- Only modules required for business analytics are included.
- Operational modules unrelated to supply chain are excluded.
- All selected DocTypes support REST API extraction.
- Every selected DocType includes a `modified` timestamp for incremental loading.
- Master data will be extracted before transactional data.
- Each DocType maps directly to a Bronze table in PostgreSQL.

---

# Phase 3 Impact

This module mapping directly determines:

- REST API endpoints
- ETL extraction order
- Bronze layer schema
- Source-to-target mapping
- dbt staging models
- Star schema design

Every ETL job implemented in Phase 3 will reference this document.

---

# Key Takeaways

- The project uses a validated set of ERPNext master, transaction, and child DocTypes required for Version 1 analytics.
- Only supply chain modules are included.
- Extraction order is based on business dependencies.
- Incremental loading will use the `modified` timestamp.
- Each source DocType maps to a dedicated Bronze table.

---

