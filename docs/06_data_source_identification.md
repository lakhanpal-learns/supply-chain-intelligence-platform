# Data Source Identification

## Project

Supply Chain Intelligence Platform

---

# Document Information

| Field | Value |
|-------|-------|
| Document Type | Data Source Identification |
| Version | 1.0 |
| Status | Draft |
| Project | Supply Chain Intelligence Platform |
| Prepared By | Lakhanpal |
| Last Updated | July 2026 |

---

# Purpose

The purpose of this document is to identify and evaluate all data sources required for the Supply Chain Intelligence Platform.

This document defines where business data originates, how it will be accessed, what information will be extracted, and how the source system supports the analytics requirements identified during Phase 1.

The output of this phase serves as the foundation for designing the ETL pipeline, PostgreSQL data warehouse, and Power BI dashboards.

---

# Phase Objectives

The objectives of Data Source Identification are to:

- Identify the operational source system.
- Understand the source system architecture.
- Determine required business entities.
- Identify data extraction methods.
- Define data ownership.
- Evaluate source system capabilities and limitations.
- Prepare for ETL pipeline development.

---

# Selected Source System

The project uses **ERPNext** as the operational Enterprise Resource Planning (ERP) system.

ERPNext was selected because it provides comprehensive supply chain functionality while exposing standardized REST APIs suitable for automated data extraction.

The application is deployed locally using the official **Frappe Docker** environment, providing complete administrative control and a stable development environment.

---

# Source System Overview

ERPNext manages all operational business transactions required for this project.

The platform records and maintains data related to:

- Suppliers
- Products
- Customers
- Warehouses
- Inventory
- Purchase Orders
- Purchase Receipts
- Stock Movements
- Sales Orders
- Delivery Notes
- Returns

These operational records will serve as the single source of truth for downstream analytics.

---

# Source System Architecture

```text
                    Users
                       │
                       ▼
                 ERPNext Web UI
                       │
                       ▼
               ERPNext Application
                       │
                REST API Layer
                       │
                       ▼
                  MariaDB Database
```

The analytics platform will not connect directly to the MariaDB database.

Instead, all operational data will be extracted through the official ERPNext REST APIs.

This approach:

- Reduces coupling with the ERP database.
- Uses supported integration mechanisms.
- Simplifies future upgrades.
- Reflects industry-standard integration practices.

---

# Business Data Required

The following business domains were identified during Phase 1.

| Business Domain | Required Data |
|-----------------|---------------|
| Procurement | Suppliers, Purchase Orders, Purchase Receipts |
| Inventory | Items, Warehouses, Inventory Levels |
| Warehouse | Stock Entries, Inventory Movements |
| Sales | Customers, Sales Orders, Delivery Notes |
| Logistics | Deliveries, Shipment Information |
| Returns | Returned Products, Return Reasons |

---

# Data Sources

| Source | Type | Priority |
|---------|------|----------|
| ERPNext REST API | Primary | High |
| ERPNext Metadata | Reference | Medium |
| Configuration Files | Supporting | Low |

Version 1 of the project relies exclusively on ERPNext as the operational source system.

External APIs and third-party datasets are outside the scope of this release.

---

# Data Access Method

Operational data will be accessed through ERPNext REST APIs.

Characteristics include:

- HTTPS communication
- JSON responses
- Token-based authentication
- Pagination support
- Filtering
- Incremental extraction using modification timestamps

No direct SQL queries will be executed against the ERP production database.

---

# Data Ownership

| Business Area | System Owner |
|---------------|-------------|
| Procurement | ERPNext |
| Inventory | ERPNext |
| Warehouse | ERPNext |
| Sales | ERPNext |
| Logistics | ERPNext |
| Returns | ERPNext |

ERPNext acts as the authoritative operational data source for all analytics.

---

# High-Level Data Flow

```text
ERPNext
      │
REST API
      │
Python ETL
      │
PostgreSQL Bronze Layer
      │
Silver Layer
      │
Gold Layer
      │
Power BI
```

This layered architecture separates operational processing from analytical workloads.

---

# Source System Constraints

The following constraints were identified.

- Data extraction depends on API availability.
- API authentication is required.
- Operational data quality directly affects downstream analytics.
- Historical records depend on ERPNext data retention.
- API response times may vary with data volume.

These constraints will be addressed during ETL development.

---

# Assumptions

The project assumes that:

- ERPNext remains available during extraction.
- REST APIs remain enabled.
- API credentials remain valid.
- Business users maintain accurate operational data.
- Daily data refresh satisfies reporting requirements.

---

# Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| API changes | High | Version-controlled API client |
| Missing business data | Medium | Data validation during ETL |
| Authentication failure | Medium | Secure credential management |
| Network interruption | Medium | Retry mechanism and logging |
| Poor operational data quality | High | Validation and quality checks |

---

# Deliverables

Phase 2 produces the following outputs.

- Source System Analysis
- ERPNext Module Mapping
- API Mapping
- Source-to-Target Mapping
- Data Extraction Strategy

These deliverables provide the blueprint for Phase 3 (ETL Development).

---

# Key Decisions

The following architectural decisions were finalized during this phase.

- ERPNext is the operational source system.
- Official Frappe Docker deployment is used.
- REST APIs are the only extraction interface.
- MariaDB is not queried directly.
- PostgreSQL is reserved exclusively for analytics.
- Incremental extraction will use the `modified` timestamp.

---

# Phase Summary

Phase 2 establishes a clear understanding of the operational data landscape.

By identifying the source system, business entities, extraction methods, and architectural constraints before implementation, the project minimizes development risk and ensures that subsequent ETL pipelines align with business requirements and industry best practices.

---
