# Stakeholder Analysis

## Project

Supply Chain Intelligence Platform

---

# Purpose

The purpose of this document is to identify all stakeholders involved in the Supply Chain Intelligence Platform and define their roles, responsibilities, business objectives, key performance indicators (KPIs), and interactions with the system.

Understanding stakeholder needs ensures that the platform delivers meaningful insights to every business function.

---

# Stakeholder Overview

| Stakeholder | Department | Role |
|-------------|------------|------|
| Chief Executive Officer (CEO) | Executive | Strategic Decision Making |
| Chief Operating Officer (COO) | Operations | Operational Performance |
| Procurement Manager | Procurement | Supplier & Purchasing Management |
| Inventory Manager | Inventory | Inventory Optimization |
| Warehouse Manager | Warehouse | Warehouse Operations |
| Logistics Manager | Logistics | Transportation & Delivery |
| Sales Manager | Sales | Order Fulfillment |
| Finance Manager | Finance | Cost & Profitability |
| Data Engineer | Technology | Data Platform Development |
| Data Analyst | Technology | Business Analytics & Reporting |

---

# Stakeholder Details

---

## 1. Chief Executive Officer (CEO)

### Responsibilities

- Monitor business performance
- Review operational KPIs
- Improve profitability
- Approve strategic initiatives

### Business Goals

- Increase revenue
- Reduce operational costs
- Improve customer satisfaction
- Improve supply chain efficiency

### Required KPIs

- Total Revenue
- Gross Profit
- Inventory Value
- Inventory Turnover
- Fill Rate
- Order Fulfillment Rate
- On-Time Delivery
- Overall Supply Chain Health

### Dashboard Usage

Executive Overview Dashboard

---

## 2. Chief Operating Officer (COO)

### Responsibilities

- Manage end-to-end supply chain operations
- Improve operational efficiency
- Monitor business performance

### Business Goals

- Reduce operational delays
- Improve warehouse efficiency
- Improve delivery performance

### Required KPIs

- Order Cycle Time
- Warehouse Utilization
- Inventory Turnover
- Transportation Cost
- Supplier Performance
- Perfect Order Rate

### Dashboard Usage

Executive Dashboard

Operations Dashboard

---

## 3. Procurement Manager

### Responsibilities

- Manage suppliers
- Purchase inventory
- Negotiate contracts
- Monitor supplier performance

### Business Goals

- Reduce procurement cost
- Improve supplier reliability
- Shorten lead times

### Required KPIs

- Supplier Spend
- Purchase Orders
- Lead Time
- Supplier Performance
- Supplier Defect Rate
- Purchase Cycle Time

### Dashboard Usage

Procurement Analytics

---

## 4. Inventory Manager

### Responsibilities

- Monitor inventory
- Prevent stockouts
- Reduce excess inventory

### Business Goals

- Optimize inventory levels
- Improve inventory turnover
- Reduce dead stock

### Required KPIs

- Current Inventory
- Inventory Value
- Safety Stock
- Reorder Point
- Inventory Aging
- Dead Stock
- Overstock
- Stockout Rate

### Dashboard Usage

Inventory Analytics

---

## 5. Warehouse Manager

### Responsibilities

- Manage warehouse operations
- Track inventory movement
- Improve warehouse utilization

### Business Goals

- Increase warehouse efficiency
- Improve storage utilization
- Reduce handling delays

### Required KPIs

- Warehouse Capacity
- Warehouse Utilization
- Inventory by Warehouse
- Inbound Shipments
- Outbound Shipments
- Stock Movements

### Dashboard Usage

Warehouse Dashboard

---

## 6. Logistics Manager

### Responsibilities

- Manage deliveries
- Monitor carriers
- Reduce transportation cost

### Business Goals

- Deliver orders on time
- Reduce shipping cost
- Improve carrier performance

### Required KPIs

- Shipment Count
- Average Delivery Time
- Transportation Cost
- Carrier Performance
- On-Time Delivery
- Delivery Delay

### Dashboard Usage

Logistics Dashboard

---

## 7. Sales Manager

### Responsibilities

- Manage customer orders
- Improve order fulfillment
- Reduce cancellations

### Business Goals

- Increase customer satisfaction
- Improve order completion
- Reduce backorders

### Required KPIs

- Orders by Status
- Fill Rate
- Perfect Order Rate
- Order Cycle Time
- Backorders
- Cancellation Rate

### Dashboard Usage

Sales & Order Fulfillment Dashboard

---

## 8. Finance Manager

### Responsibilities

- Monitor operational spending
- Analyze profitability
- Control procurement cost

### Business Goals

- Improve profit margin
- Reduce operational expenses
- Optimize inventory investment

### Required KPIs

- Revenue
- Procurement Spend
- Transportation Cost
- Inventory Value
- Return Cost
- Gross Margin

### Dashboard Usage

Executive Dashboard

Financial Reports

---

## 9. Data Engineer

### Responsibilities

- Build ETL pipelines
- Develop database
- Maintain data quality
- Schedule workflows
- Monitor pipelines

### Business Goals

- Reliable data ingestion
- High-quality datasets
- Automated processing
- Stable infrastructure

### Tools

- Python
- PostgreSQL
- dbt
- Docker
- Apache Airflow

---

## 10. Data Analyst

### Responsibilities

- Develop dashboards
- Analyze KPIs
- Generate insights
- Support business decisions

### Business Goals

- Deliver accurate reporting
- Identify trends
- Recommend improvements

### Tools

- SQL
- Power BI
- PostgreSQL

---

# Stakeholder Communication Matrix

| Stakeholder | Dashboard | Reporting Frequency |
|-------------|-----------|---------------------|
| CEO | Executive Dashboard | Daily |
| COO | Operations Dashboard | Daily |
| Procurement Manager | Procurement Dashboard | Daily |
| Inventory Manager | Inventory Dashboard | Daily |
| Warehouse Manager | Warehouse Dashboard | Daily |
| Logistics Manager | Logistics Dashboard | Daily |
| Sales Manager | Sales Dashboard | Daily |
| Finance Manager | Executive Dashboard | Weekly |
| Data Engineer | Pipeline Monitoring | Daily |
| Data Analyst | Business Dashboards | Daily |

---

# Stakeholder Data Requirements

| Department | Required Data |
|------------|---------------|
| Procurement | Purchase Orders, Suppliers, Purchase Receipts |
| Inventory | Stock Levels, Items, Warehouses |
| Warehouse | Stock Movements, Inventory |
| Logistics | Deliveries, Shipments, Carriers |
| Sales | Sales Orders, Customers |
| Finance | Revenue, Procurement Cost, Transportation Cost |

---

# Stakeholder Success Metrics

The platform will be considered successful if stakeholders can:

- Access a single source of truth for supply chain data.
- Monitor KPIs through interactive dashboards.
- Reduce manual reporting effort.
- Detect operational issues quickly.
- Make faster, data-driven decisions.
- Improve supply chain performance over time.

---

# Key Takeaways

- Executives require high-level strategic KPIs.
- Operational managers require detailed functional dashboards.
- Technical teams require reliable, automated, and well-documented data pipelines.
- The platform must support different stakeholder needs while maintaining a single, trusted data source.

---

# Next Document

The next document is **04_supply_chain_process.md**, where we will map the complete business process from supplier procurement to customer delivery and returns. This process map will directly determine the ERPNext modules, APIs, and database tables used in the ETL pipeline.