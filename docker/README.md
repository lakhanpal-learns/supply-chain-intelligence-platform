# Docker Infrastructure

## Purpose

This directory contains the Docker infrastructure for the **Supply Chain Intelligence Platform**.

Instead of installing each service manually, Docker Compose orchestrates all required services into a unified development environment.

The infrastructure is designed to be reproducible, portable, and easy to set up for any developer.

---

# Services

The platform consists of the following services:

| Service | Purpose |
|----------|---------|
| ERPNext | Source ERP System |
| MariaDB | ERPNext Transactional Database |
| Redis | Cache & Background Queue |
| PostgreSQL | Analytics Data Warehouse |
| Apache Airflow | Workflow Orchestration |

---

# Architecture

```text
                +----------------------+
                |      ERPNext         |
                +----------+-----------+
                           |
                     REST API
                           |
                           ▼
                 Python ETL Pipeline
                           |
                           ▼
              PostgreSQL Data Warehouse
                           |
                     dbt Models
                           |
                           ▼
                 Power BI Dashboards
```

---

# Development Philosophy

This project follows a production-inspired architecture.

- ERPNext remains the operational system (OLTP).
- PostgreSQL acts as the analytical warehouse (OLAP).
- Airflow automates ETL pipelines.
- Docker Compose manages all infrastructure.

---

# Startup Goal

The long-term goal is to launch the complete analytics platform with a single command:

```bash
docker compose up -d
```

---

# Current Status

- [x] Docker Installed
- [x] WSL2 Configured
- [ ] Docker Compose Infrastructure
- [ ] ERPNext Running
- [ ] PostgreSQL Running
- [ ] Airflow Running

---

# Next Steps

1. Build Docker Compose.
2. Deploy ERPNext.
3. Configure PostgreSQL.
4. Configure Airflow.
5. Build ETL pipeline.