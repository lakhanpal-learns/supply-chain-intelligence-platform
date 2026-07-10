# Source System Overview

## Project

Supply Chain Intelligence Platform

---

# Document Information

| Field | Value |
|-------|-------|
| Document Type | Source System Overview |
| Version | 1.0 |
| Status | Draft |
| Project | Supply Chain Intelligence Platform |
| Prepared By | Lakhanpal |
| Last Updated | July 2026 |

---

# Purpose

The purpose of this document is to provide a comprehensive technical overview of the operational source system used by the Supply Chain Intelligence Platform.

Understanding the architecture, deployment model, data storage, and integration capabilities of the source system is essential before designing ETL pipelines and analytics infrastructure.

This document explains how ERPNext stores operational data, how external systems access that data, and why the chosen integration approach aligns with modern data engineering best practices.

---

# Source System

The operational source system for this project is **ERPNext**, an open-source Enterprise Resource Planning (ERP) platform developed by Frappe Technologies.

ERPNext provides integrated business modules for procurement, inventory, warehouse management, sales, finance, manufacturing, human resources, and customer relationship management.

For this project, ERPNext serves as the organization's Online Transaction Processing (OLTP) system, where day-to-day business transactions are recorded.

---

# Why ERPNext?

ERPNext was selected because it satisfies both business and technical requirements.

## Business Advantages

- Complete supply chain management
- Integrated procurement and inventory workflows
- End-to-end order lifecycle management
- Standardized business processes
- Rich operational reporting

---

## Technical Advantages

- Official REST API support
- Open-source platform
- Docker deployment
- Well-documented architecture
- JSON-based API responses
- Active community support
- Suitable for ETL integration

---

# Deployment Architecture

The project uses the official Docker deployment provided by the Frappe project.

The ERP environment runs locally, providing complete administrative control and a reproducible development environment.

The deployment consists of multiple cooperating containers rather than a single application container.

---

# ERPNext Architecture

```text
                    Users
                       │
                       ▼
                 ERPNext Frontend
                       │
                       ▼
                 ERPNext Backend
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
    MariaDB       Redis Cache    Redis Queue
        │
        ▼
 Business Data
```

---

# Core Components

## Frontend

Provides the web interface used by business users.

Responsibilities include:

- User authentication
- Dashboard rendering
- Form management
- API request routing

---

## Backend

The backend contains the business logic of ERPNext.

Responsibilities include:

- Business rule execution
- API processing
- Database interaction
- Permission validation
- Workflow execution

---

## MariaDB

MariaDB stores all operational business data.

Examples include:

- Items
- Suppliers
- Customers
- Purchase Orders
- Sales Orders
- Delivery Notes
- Inventory
- Warehouses

MariaDB functions as the transactional database (OLTP).

The analytics platform will not query MariaDB directly.

---

## Redis

ERPNext uses Redis for several internal services.

### Redis Cache

Stores frequently accessed information to improve application performance.

---

### Redis Queue

Handles background jobs such as report generation, scheduled tasks, and asynchronous processing.

---

### Redis SocketIO

Supports real-time communication between the server and connected users.

---

# ERPNext Modules Used

Version 1 of this project focuses on the following ERP modules.

| Module | Business Purpose |
|----------|------------------|
| Supplier | Supplier Management |
| Item | Product Master |
| Warehouse | Warehouse Management |
| Bin | Inventory Levels |
| Purchase Order | Procurement |
| Purchase Receipt | Goods Receipt |
| Stock Entry | Inventory Movement |
| Customer | Customer Management |
| Sales Order | Customer Orders |
| Delivery Note | Order Fulfillment |

Modules outside the project scope, such as Manufacturing, HR, CRM, and Projects, are intentionally excluded.

---

# Data Storage Model

ERPNext organizes business information into **DocTypes**.

Each DocType represents a business entity.

Examples include:

| Business Entity | ERPNext DocType |
|-----------------|-----------------|
| Product | Item |
| Supplier | Supplier |
| Customer | Customer |
| Warehouse | Warehouse |
| Purchase Order | Purchase Order |
| Sales Order | Sales Order |

Each DocType stores both business data and metadata, including creation timestamps and modification timestamps.

---

# Integration Method

The Supply Chain Intelligence Platform integrates with ERPNext through its official REST APIs.

The integration follows this architecture.

```text
ERPNext
     │
REST API
     │
Python ETL
     │
Analytics Warehouse
```

Direct database access is intentionally avoided.

This approach provides:

- Loose coupling
- Better maintainability
- Version compatibility
- Improved security
- Vendor-supported integration

---

# REST API Characteristics

ERPNext exposes resources through REST endpoints.

Characteristics include:

- HTTPS communication
- JSON responses
- GET, POST, PUT and DELETE operations
- Filtering
- Pagination
- Field selection
- Ordering
- Authentication

The project primarily uses GET requests during ETL extraction.

---

# Authentication

ERPNext supports multiple authentication mechanisms.

For this project, API authentication will be implemented using secure API credentials generated within ERPNext.

Credentials will be stored outside the application code using environment variables.

---

# Incremental Data Support

ERPNext automatically maintains important audit fields.

Examples include:

- creation
- modified
- owner
- modified_by

The **modified** timestamp will be used for incremental data extraction, allowing the ETL pipeline to retrieve only newly created or updated records.

---

# Operational Characteristics

| Characteristic | Description |
|----------------|-------------|
| Data Type | Transactional (OLTP) |
| Database | MariaDB |
| Integration | REST API |
| Response Format | JSON |
| Deployment | Docker |
| Authentication | API Credentials |
| Incremental Support | Modified Timestamp |

---

# System Limitations

The following operational considerations influence ETL design.

- API availability determines extraction success.
- Business data quality depends on user input.
- Large datasets require pagination.
- Network interruptions must be handled gracefully.
- Authentication failures must be logged and retried.

These limitations will be addressed during ETL implementation.

---

# Architectural Decision

The project intentionally separates operational and analytical workloads.

```text
Operational System (OLTP)

ERPNext
    │
MariaDB

            │

            ▼

Analytics Platform (OLAP)

Python ETL
    │
PostgreSQL
    │
dbt
    │
Power BI
```

This separation prevents analytical processing from affecting operational system performance.

---

# Key Takeaways

- ERPNext is the authoritative operational system.
- MariaDB stores transactional business data.
- REST APIs provide the official integration interface.
- Python ETL will extract data without modifying ERPNext.
- PostgreSQL will function as the analytical data warehouse.
- The architecture follows modern data engineering best practices.

---

