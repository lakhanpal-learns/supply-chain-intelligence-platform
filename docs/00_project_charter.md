# Project Charter

## Project Information

| Field | Value |
|------|------|
| Project Name | Supply Chain Intelligence Platform |
| Project Type | End-to-End Data Engineering & Analytics Portfolio |
| Version | 1.0 |
| Status | In Progress |
| Project Owner | Lakhanpal |
| Start Date | July 2026 |
| End Date | TBD |

---

# Executive Summary

The **Supply Chain Intelligence Platform** is an end-to-end data engineering and analytics project designed to demonstrate how modern organizations transform operational ERP data into actionable business intelligence.

The platform extracts transactional data from ERPNext using REST APIs, processes it through an automated ETL pipeline, stores it in PostgreSQL using a multi-layer architecture, transforms it into an analytics-ready star schema using dbt, and presents business insights through interactive Power BI dashboards.

The project follows industry-standard data engineering and analytics practices, emphasizing automation, scalability, documentation, and business value.

---

# Vision

Build a production-style analytics platform that enables business users to monitor and optimize the complete supply chain lifecycle through reliable, automated, and data-driven reporting.

---

# Business Objective

Provide stakeholders with a centralized platform capable of monitoring procurement, inventory, warehouse operations, logistics, sales, and returns using trusted data and meaningful KPIs.

---

# Problem Statement

Organizations often rely on fragmented ERP reports and spreadsheets, leading to:

- Limited operational visibility
- Manual reporting
- Delayed decision-making
- Poor inventory optimization
- Supplier performance challenges
- Inconsistent KPI reporting

This project addresses these challenges by building a unified analytics platform.

---

# Project Scope

## Included

- ERPNext REST API Integration
- Python ETL Pipelines
- Incremental Data Loading
- PostgreSQL Database
- Bronze, Silver, and Gold Data Layers
- Data Quality Validation
- SQL & dbt Transformations
- Star Schema Data Warehouse
- Apache Airflow Scheduling
- Dockerized Environment
- Power BI Dashboards
- Technical Documentation

---

## Excluded (Version 1)

- Machine Learning
- Demand Forecasting
- Manufacturing Analytics
- Real-time Streaming
- Multi-cloud Deployment
- ERP Write-back Operations
- Mobile Applications

---

# Project Goals

- Automate ERP data extraction.
- Build a reliable ETL pipeline.
- Design a scalable analytics warehouse.
- Develop business-focused dashboards.
- Calculate supply chain KPIs accurately.
- Automate daily pipeline execution.
- Follow modern data engineering best practices.
- Produce professional project documentation.

---

# Stakeholders

| Stakeholder | Responsibility |
|-------------|----------------|
| CEO | Strategic Decision Making |
| COO | Operations Management |
| Procurement Manager | Supplier Management |
| Inventory Manager | Inventory Control |
| Warehouse Manager | Warehouse Operations |
| Logistics Manager | Transportation Management |
| Sales Manager | Order Fulfillment |
| Finance Manager | Financial Analysis |
| Data Engineer | Platform Development |
| Data Analyst | Reporting & Insights |

---

# Technology Stack

| Layer | Technology |
|------|------------|
| ERP System | ERPNext |
| Programming Language | Python |
| Database | PostgreSQL |
| Data Transformation | dbt |
| Workflow Orchestration | Apache Airflow |
| Containerization | Docker |
| Business Intelligence | Power BI |
| Version Control | Git & GitHub |

---

# High-Level Architecture

```text
                ERPNext REST API
                        │
                        ▼
               Python ETL Pipeline
                        │
                        ▼
          PostgreSQL Bronze (Raw Layer)
                        │
                        ▼
        Data Validation & Quality Checks
                        │
                        ▼
         PostgreSQL Silver (Clean Layer)
                        │
                        ▼
         dbt Business Transformations
                        │
                        ▼
         PostgreSQL Gold (Star Schema)
                        │
                        ▼
             Power BI Dashboards
                        │
                        ▼
            Business Decision Making
```

---

# Major Deliverables

## Data Engineering

- ERPNext API Integration
- ETL Pipeline
- PostgreSQL Database
- Bronze Layer
- Silver Layer
- Gold Layer
- Data Quality Framework
- dbt Models
- Airflow DAG
- Docker Configuration

---

## Analytics

- Executive Dashboard
- Procurement Dashboard
- Inventory Dashboard
- Warehouse Dashboard
- Logistics Dashboard
- Sales Dashboard
- Returns Dashboard

---

## Documentation

- Project Charter
- Business Documentation
- Data Dictionary
- API Documentation
- ETL Documentation
- Architecture Diagram
- Database Schema
- KPI Definitions
- Dashboard Guide
- Deployment Guide

---

# Success Criteria

The project will be considered successful when:

- ERPNext data is extracted successfully.
- ETL pipelines execute automatically.
- Data quality checks pass.
- Analytics warehouse is implemented.
- KPIs are calculated correctly.
- Dashboards provide actionable business insights.
- Documentation enables another developer to reproduce the project.

---

# Expected Business Outcomes

- Centralized reporting
- Faster decision-making
- Improved supplier monitoring
- Better inventory management
- Increased warehouse visibility
- Improved logistics performance
- Reduced manual reporting effort

---

# Project Timeline

| Phase | Status |
|------|--------|
| Phase 1 – Business Understanding | ✅ Completed |
| Phase 2 – Data Source Identification | ⏳ Pending |
| Phase 3 – Data Ingestion | ⏳ Pending |
| Phase 4 – Raw Data Storage | ⏳ Pending |
| Phase 5 – Data Validation & Quality | ⏳ Pending |
| Phase 6 – Data Cleaning | ⏳ Pending |
| Phase 7 – Data Transformation | ⏳ Pending |
| Phase 8 – Data Modeling | ⏳ Pending |
| Phase 9 – Data Warehouse | ⏳ Pending |
| Phase 10 – Data Serving | ⏳ Pending |
| Phase 11 – Analytics & Consumption | ⏳ Pending |
| Phase 12 – Monitoring & Operations | ⏳ Pending |
| Phase 13 – Governance & Security | ⏳ Pending |

---

# Project Repository Structure

```text
Supply-Chain-Intelligence-Platform/
│
├── api/
├── etl/
├── database/
├── dbt/
├── airflow/
├── powerbi/
├── docs/
├── tests/
├── docker/
├── requirements.txt
├── docker-compose.yml
└── README.md
```

---

# Key Principles

This project follows four guiding principles:

1. **Business First** – Every technical component must solve a real business problem.
2. **Automation by Design** – Manual work should be minimized through automated pipelines.
3. **Scalable Architecture** – The solution should be easy to extend with additional modules and KPIs.
4. **Production-Oriented Development** – Code, documentation, testing, and project organization should reflect industry practices.

---

# Approval

| Role | Status |
|------|--------|
| Project Owner | Approved |
| Business Review | Pending |
| Technical Review | Pending |