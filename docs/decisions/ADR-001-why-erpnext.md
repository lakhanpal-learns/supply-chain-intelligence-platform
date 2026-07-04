## Decision

We will use a locally hosted ERPNext instance running in Docker as the primary source system for the Supply Chain Intelligence Platform.

## Context

The project requires a realistic ERP system capable of generating procurement, inventory, warehouse, sales, logistics, and customer data.

## The source system must:

Support REST APIs
Allow complete administrative control
Support incremental extraction
Be reproducible by other developers
Integrate with Docker-based infrastructure

## Several options were evaluated:

Public ERPNext Demo
Local ERPNext using Docker
Cloud-hosted ERPNext

## Decision

The project will use a local ERPNext instance deployed with Docker.

## Rationale
• Full administrative control
• Stable and reproducible dataset
• Ability to create realistic business scenarios
• Supports incremental ETL development
• Seamless integration with Docker
• No dependency on public demo availability
• Enables comprehensive data quality testing
• Easier debugging during development

## Consequences
### Positive

• Complete control over ERP data
• Stable development environment
• Better portfolio quality
• Easier testing
• Supports future automation

## Negative
• Initial setup complexity
• Requires local system resources
• Docker environment maintenance

## status

Accepted

Date: July 2026