# ERPNext Module Mapping

## Project

Supply Chain Intelligence Platform

---

# Document Information

| Field | Value |
|-------|-------|
| Document Type | ERPNext Module Mapping |
| Version | 1.0 |
| Status | Draft |
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
Purchase Receipt
      │
      ▼
Warehouse Inventory
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
Customer
      │
      ▼
Returns
```

---

# ERPNext Module Mapping

| Business Process | ERP Module | ERPNext DocType | Priority | Incremental Field | Target Bronze Table |
|------------------|------------|-----------------|----------|------------------|---------------------|
| Supplier Management | Buying | Supplier | High | modified | bronze_supplier |
| Product Management | Stock | Item | High | modified | bronze_item |
| Warehouse Management | Stock | Warehouse | High | modified | bronze_warehouse |
| Inventory Management | Stock | Bin | High | modified | bronze_bin |
| Purchase Requests | Buying | Material Request | Medium | modified | bronze_material_request |
| Purchase Orders | Buying | Purchase Order | High | modified | bronze_purchase_order |
| Purchase Receipts | Buying | Purchase Receipt | High | modified | bronze_purchase_receipt |
| Inventory Movement | Stock | Stock Entry | High | modified | bronze_stock_entry |
| Customer Management | Selling | Customer | High | modified | bronze_customer |
| Sales Orders | Selling | Sales Order | High | modified | bronze_sales_order |
| Deliveries | Selling | Delivery Note | High | modified | bronze_delivery_note |

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
```

These relationships define the order in which data should be extracted and later transformed.

---

# Data Dependencies

Certain DocTypes depend on others.

| Parent Entity | Child Entity | Dependency |
|---------------|--------------|------------|
| Supplier | Purchase Order | Supplier must exist first |
| Item | Purchase Order | Product must exist first |
| Purchase Order | Purchase Receipt | Purchase Order reference |
| Warehouse | Bin | Warehouse reference |
| Item | Bin | Product reference |
| Customer | Sales Order | Customer reference |
| Sales Order | Delivery Note | Sales Order reference |

These dependencies will determine the ETL extraction sequence.

---

# Recommended Extraction Order

The ETL pipeline should extract data in the following order.

| Step | DocType | Reason |
|------|----------|--------|
| 1 | Supplier | Master Data |
| 2 | Customer | Master Data |
| 3 | Item | Master Data |
| 4 | Warehouse | Master Data |
| 5 | Bin | Inventory Snapshot |
| 6 | Material Request | Procurement Planning |
| 7 | Purchase Order | Procurement Transactions |
| 8 | Purchase Receipt | Goods Receipt |
| 9 | Stock Entry | Inventory Movement |
| 10 | Sales Order | Sales Transactions |
| 11 | Delivery Note | Fulfillment |

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

- Eleven ERPNext DocTypes have been selected for Version 1.
- Only supply chain modules are included.
- Extraction order is based on business dependencies.
- Incremental loading will use the `modified` timestamp.
- Each source DocType maps to a dedicated Bronze table.

---

