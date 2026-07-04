# Phase 1: Business Understanding

## Project Overview

The Supply Chain Intelligence Platform is an end-to-end analytics solution designed to transform operational data from ERPNext into actionable business insights. The platform integrates data engineering and business intelligence practices to provide decision-makers with a centralized view of procurement, inventory, warehouse operations, logistics, sales, and overall supply chain performance.

The primary objective is to build a production-style analytics platform that demonstrates modern data engineering techniques while solving real-world supply chain business problems.

---

# Business Background

GlobalMart Retail Pvt. Ltd. is a fictional retail distribution company that purchases products from multiple suppliers, stores inventory across regional warehouses, and fulfills customer orders through both retail and online channels.

As business operations continue to grow, the company generates large volumes of transactional data every day. Although ERPNext stores this information, management currently relies on manual reports and spreadsheets for decision-making. This results in delayed reporting, fragmented visibility, and inefficient operational planning.

To improve operational efficiency and support data-driven decision-making, the company requires a centralized analytics platform capable of consolidating supply chain data into meaningful dashboards and performance indicators.

---

# Business Problem

The organization currently faces several operational challenges throughout its supply chain.

### Procurement Challenges

- Limited visibility into supplier performance
- Delayed supplier deliveries
- Increasing procurement costs
- Difficulty tracking purchase order performance

### Inventory Challenges

- Overstocked inventory increasing holding costs
- Frequent stock shortages affecting customer satisfaction
- Limited visibility into inventory turnover
- Dead and slow-moving inventory occupying warehouse space

### Warehouse Challenges

- Uneven warehouse utilization
- Limited visibility into stock movement
- Difficulty monitoring inbound and outbound operations

### Sales & Fulfillment Challenges

- Delayed order fulfillment
- Increasing backorders
- Difficulty tracking perfect order rates
- Limited visibility into order cycle times

### Logistics Challenges

- Late customer deliveries
- High transportation costs
- Inconsistent carrier performance
- Limited shipment tracking analytics

### Executive Challenges

- Reports generated manually
- Multiple disconnected data sources
- Lack of centralized KPI monitoring
- Slow business decision-making

---

# Project Objective

Develop a centralized Supply Chain Intelligence Platform that collects operational data from ERPNext, processes it through an automated ETL pipeline, stores it in a PostgreSQL analytics warehouse, and presents actionable business insights through Power BI dashboards.

The platform will enable business users to monitor supply chain performance using reliable, accurate, and timely data.

---

# Project Goals

The project aims to achieve the following objectives:

- Automate data extraction from ERPNext REST APIs.
- Build a scalable ETL pipeline using Python.
- Store raw operational data inside PostgreSQL.
- Transform transactional data into analytics-ready datasets using dbt.
- Design a dimensional data warehouse using a star schema.
- Build interactive Power BI dashboards for business users.
- Automate daily pipeline execution using Apache Airflow.
- Containerize the project using Docker for portability.
- Maintain comprehensive technical and business documentation.

---

# Business Value

The platform will provide measurable value across multiple departments.

## Executive Management

- Centralized supply chain visibility
- Faster strategic decision-making
- Executive KPI dashboards

## Procurement Team

- Supplier performance monitoring
- Procurement cost analysis
- Lead time tracking

## Inventory Team

- Inventory optimization
- Stockout monitoring
- Overstock identification
- Inventory turnover analysis

## Warehouse Team

- Warehouse utilization analysis
- Inventory movement tracking
- Capacity monitoring

## Logistics Team

- Carrier performance analysis
- Delivery tracking
- Transportation cost monitoring

## Sales Team

- Order fulfillment tracking
- Backorder monitoring
- Customer service improvement

---

# Expected Outcomes

Upon completion, the organization will be able to:

- Monitor the complete supply chain from procurement to delivery.
- Track business KPIs through interactive dashboards.
- Reduce manual reporting efforts.
- Improve inventory planning.
- Identify operational bottlenecks.
- Support faster and more informed business decisions.
- Maintain historical operational data for trend analysis.

---

# Project Scope

## In Scope

- ERPNext REST API integration
- Incremental ETL pipeline
- PostgreSQL data warehouse
- Data validation and cleaning
- SQL transformations
- dbt models
- Star schema design
- Power BI dashboards
- Airflow scheduling
- Docker deployment
- Technical documentation

## Out of Scope (Version 1)

- Machine Learning models
- Demand forecasting
- Manufacturing analytics
- Real-time streaming pipelines
- Multi-cloud deployment
- Mobile application development
- ERP data modification (write-back)

---

# Technology Stack

| Category | Technology |
|----------|------------|
| ERP System | ERPNext |
| Programming Language | Python |
| Database | PostgreSQL |
| Data Transformation | dbt |
| Workflow Orchestration | Apache Airflow |
| Containerization | Docker |
| Business Intelligence | Power BI |
| Version Control | Git & GitHub |

---

# Success Criteria

The project will be considered successful when:

- Data is extracted automatically from ERPNext.
- Incremental ETL pipelines execute successfully.
- Data quality checks pass without critical errors.
- Business data is transformed into a star schema.
- KPIs are calculated accurately.
- Power BI dashboards refresh successfully.
- Airflow automates pipeline execution.
- Documentation enables another developer to reproduce the project.

---

# Supply Chain Process Overview

```text
Suppliers
    │
    ▼
Purchase Orders
    │
    ▼
Purchase Receipts
    │
    ▼
Warehouses
    │
    ▼
Inventory
    │
    ▼
Sales Orders
    │
    ▼
Delivery
    │
    ▼
Customers
    │
    ▼
Returns
```

---

# Next Phase

The next phase focuses on **Data Source Identification**, where the ERPNext data model will be analyzed to determine the required APIs, business entities, relationships, and extraction strategy for the ETL pipeline.