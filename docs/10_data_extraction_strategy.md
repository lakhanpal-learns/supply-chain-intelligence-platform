# Data Extraction Strategy

## Project

Supply Chain Intelligence Platform

---

# Document Information

| Field | Value |
|-------|-------|
| Document Type | Data Extraction Strategy |
| Version | 1.0 |
| Status | Draft |
| Project | Supply Chain Intelligence Platform |
| Prepared By | Lakhanpal |
| Last Updated | July 2026 |

---

# Purpose

The purpose of this document is to define the extraction strategy for the Supply Chain Intelligence Platform.

This document explains how operational data will be extracted from ERPNext, how extraction jobs will be executed, how failures will be handled, and how data consistency will be maintained.

The strategy provides the implementation blueprint for the ETL pipeline developed during Phase 3.

---

# ETL Strategy Overview

The ETL pipeline follows a modern batch-based extraction architecture.

```text
ERPNext REST API
        │
        ▼
Authentication
        │
        ▼
Data Extraction
        │
        ▼
Validation
        │
        ▼
Raw JSON Backup
        │
        ▼
Bronze Layer
        │
        ▼
Execution Logs
```

Each stage is isolated to simplify monitoring, debugging, and recovery.

---

# Extraction Types

Two extraction methods will be used.

## Initial Full Load

The first pipeline execution extracts all available records from each selected DocType.

Purpose:

- Populate the Bronze layer
- Establish the initial historical dataset
- Create ETL checkpoints

The full load is executed only once unless a complete rebuild is required.

---

## Incremental Load

After the initial load, only new or modified records are extracted.

The ETL pipeline compares the source system's `modified` timestamp with the most recent successful synchronization timestamp.

Benefits include:

- Reduced execution time
- Lower network usage
- Reduced API load
- Faster daily refreshes

---

# Incremental Extraction Logic

```text
Last Successful Sync
          │
          ▼
Read modified timestamp
          │
          ▼
Request records where

modified > last_sync
          │
          ▼
Load only changed records
```

This strategy minimizes unnecessary data movement while keeping the analytics warehouse synchronized.

---

# Extraction Sequence

Master data is extracted before transactional data.

| Step | DocType | Category |
|------|----------|----------|
| 1 | Supplier | Master |
| 2 | Customer | Master |
| 3 | Item | Master |
| 4 | Warehouse | Master |
| 5 | Bin | Inventory |
| 6 | Material Request | Transaction |
| 7 | Purchase Order | Transaction |
| 8 | Purchase Receipt | Transaction |
| 9 | Stock Entry | Transaction |
| 10 | Sales Order | Transaction |
| 11 | Delivery Note | Transaction |

This sequence preserves referential integrity.

---

# Extraction Workflow

```text
Start Pipeline
      │
      ▼
Authenticate
      │
      ▼
Read Configuration
      │
      ▼
Read Last Sync Timestamp
      │
      ▼
Extract Data
      │
      ▼
Validate Response
      │
      ▼
Save JSON Backup
      │
      ▼
Load Bronze Layer
      │
      ▼
Update Sync Timestamp
      │
      ▼
Write Logs
      │
      ▼
Pipeline Complete
```

---

# Checkpoint Management

Each successful extraction updates a checkpoint containing:

- DocType
- Last successful sync timestamp
- Records extracted
- Execution duration
- Pipeline status

Checkpoint information enables reliable incremental loading and recovery after failures.

---

# JSON Backup Strategy

Before loading into PostgreSQL, every API response is stored as a JSON backup.

Purpose:

- Disaster recovery
- Pipeline debugging
- Data auditing
- Historical comparison

JSON backups are temporary operational artifacts and are not intended as the primary analytical storage.

---

# Error Handling Strategy

The ETL pipeline will classify errors into the following categories.

| Error Type | Action |
|------------|--------|
| Authentication Failure | Stop pipeline |
| Network Timeout | Retry |
| API Server Error | Retry |
| Invalid Response | Log and stop current extraction |
| Empty Response | Continue |
| Database Error | Roll back current load |

---

# Retry Strategy

Transient failures will be retried automatically.

| Attempt | Waiting Time |
|----------|--------------|
| Retry 1 | 5 seconds |
| Retry 2 | 15 seconds |
| Retry 3 | 30 seconds |

After the third unsuccessful attempt, the pipeline is marked as failed and requires manual review.

---

# Logging Strategy

Each extraction records:

- Execution ID
- Pipeline start time
- Pipeline end time
- Source DocType
- Records extracted
- Execution duration
- HTTP status
- Retry attempts
- Final status

Logs provide operational visibility and support troubleshooting.

---

# Data Validation

Basic validation is performed before loading data into the Bronze layer.

Validation includes:

- Valid JSON structure
- Required fields present
- Non-empty primary keys
- Duplicate detection within response
- API response status

Comprehensive data quality checks will be implemented during Phase 5.

---

# Performance Strategy

The ETL pipeline is designed for efficient batch processing.

Techniques include:

- Pagination
- Incremental extraction
- Field selection
- Configurable batch sizes
- Reusable HTTP sessions

These optimizations reduce API latency and improve pipeline performance.

---

# Scheduling Strategy

Version 1 executes once per day.

Future execution will be automated using Apache Airflow.

```text
Airflow Scheduler
        │
        ▼
Daily ETL Pipeline
        │
        ▼
Bronze Layer Refresh
```

---

# Security Considerations

The ETL process follows these security practices.

- API credentials stored in environment variables.
- Read-only API access.
- No credentials committed to version control.
- Sensitive values excluded from logs.
- Production environments should use HTTPS.

---

# Design Decisions

The following architectural decisions were finalized.

- REST API is the only extraction interface.
- Incremental loading uses the `modified` timestamp.
- Master data precedes transactional data.
- JSON backups are created before database loading.
- Every extraction generates operational logs.
- Airflow will orchestrate future pipeline execution.

---

# Phase 3 Implementation

The following Phase 3 components will implement this strategy.

- API Client
- Authentication Module
- Incremental Loader
- Configuration Manager
- Logging Framework
- Bronze Loader

Every ETL component will follow the standards defined in this document.

---

# Key Takeaways

- Initial execution performs a full load.
- Future executions perform incremental loads.
- Data extraction is batch-oriented.
- JSON backups improve recoverability.
- Logging and checkpoints enable operational monitoring.
- The strategy is scalable and production-oriented.

---

# Phase 2 Completion

With this document, Phase 2 establishes:

- Source system identification
- ERPNext architecture understanding
- Module mapping
- API mapping
- ETL extraction strategy

These deliverables provide a complete technical blueprint for Phase 3 (ETL Development).

---

# Next Phase

**Phase 3 – ETL Development**

The next phase implements the Python ETL pipeline using the designs established during Phase 2. Development begins with the API client, configuration management, authentication, logging framework, and reusable extraction components that will populate the PostgreSQL Bronze layer.