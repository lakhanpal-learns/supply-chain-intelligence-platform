# KPI Definitions

## Project

Supply Chain Intelligence Platform

---

# Purpose

This document defines all Key Performance Indicators (KPIs) used throughout the Supply Chain Intelligence Platform.

Each KPI includes:

- Business Purpose
- Definition
- Calculation Formula
- Business Interpretation
- Data Source
- Dashboard Module
- Refresh Frequency

These KPI definitions ensure consistency across SQL transformations, dbt models, and Power BI dashboards.

---

# KPI Categories

1. Executive KPIs
2. Procurement KPIs
3. Inventory KPIs
4. Warehouse KPIs
5. Sales & Fulfillment KPIs
6. Logistics KPIs
7. Returns & Quality KPIs

---

# 1. Executive KPIs

---

## Total Revenue

### Business Purpose

Measure the total sales generated during a selected period.

### Formula

```
Sum(Sales Amount)
```

### Interpretation

Higher revenue indicates stronger business performance.

### Data Source

- Sales Order
- Sales Invoice

### Dashboard

Executive Overview

---

## Total Orders

### Business Purpose

Track customer demand.

### Formula

```
Count(Sales Orders)
```

### Dashboard

Executive Overview

---

## Inventory Value

### Business Purpose

Measure the monetary value of inventory currently stored.

### Formula

```
Σ(Current Stock × Unit Cost)
```

### Dashboard

Executive Overview
Inventory Analytics

---

## Inventory Turnover

### Business Purpose

Measure how efficiently inventory is sold.

### Formula

```
Cost of Goods Sold
------------------
Average Inventory
```

### Interpretation

Higher turnover indicates efficient inventory management.

---

## Fill Rate

### Business Purpose

Measure the percentage of customer demand fulfilled immediately.

### Formula

```
Delivered Quantity
------------------
Ordered Quantity
×100
```

---

## Order Fulfillment Rate

### Business Purpose

Measure successfully completed customer orders.

### Formula

```
Delivered Orders
----------------
Total Orders
×100
```

---

## On-Time Delivery %

### Business Purpose

Measure delivery performance.

### Formula

```
On-Time Deliveries
------------------
Total Deliveries
×100
```

---

## Supply Chain Health Score

### Business Purpose

Provide an executive summary KPI combining multiple operational metrics.

### Components

- Inventory Turnover
- Fill Rate
- On-Time Delivery
- Stockout Rate
- Supplier Performance

---

# 2. Procurement KPIs

---

## Purchase Orders

### Formula

```
Count(Purchase Orders)
```

---

## Supplier Spend

### Formula

```
Sum(Purchase Amount)
```

---

## Supplier Lead Time

### Formula

```
Purchase Receipt Date
-
Purchase Order Date
```

---

## Supplier Performance Score

### Based On

- Lead Time
- Delivery Accuracy
- Defect Rate
- Order Completion

---

## Supplier Defect Rate

### Formula

```
Rejected Quantity
-----------------
Received Quantity
×100
```

---

## Purchase Cycle Time

### Formula

```
Purchase Receipt Date
-
Purchase Request Date
```

---

# 3. Inventory KPIs

---

## Current Inventory

### Formula

```
Current Stock Quantity
```

---

## Safety Stock

Minimum inventory maintained to avoid stockouts.

---

## Reorder Point

### Formula

```
Average Daily Demand × Lead Time
+ Safety Stock
```

---

## Stockout Rate

### Formula

```
Stockout Events
---------------
Total Items
×100
```

---

## Overstock Rate

### Formula

```
Overstocked Items
-----------------
Total Items
×100
```

---

## Dead Stock

Inventory with no movement during the defined analysis period.

---

## Inventory Aging

Average number of days inventory remains in storage.

---

## ABC Classification

Inventory categorized based on annual consumption value.

| Category | Contribution |
|----------|--------------|
| A | High Value |
| B | Medium Value |
| C | Low Value |

---

# 4. Warehouse KPIs

---

## Warehouse Capacity

Maximum storage capacity.

---

## Warehouse Utilization

### Formula

```
Current Storage
---------------
Maximum Capacity
×100
```

---

## Inventory by Warehouse

Current inventory available in each warehouse.

---

## Inbound Shipments

Number of received shipments.

---

## Outbound Shipments

Number of dispatched shipments.

---

## Stock Movements

Count of inventory transfers.

---

# 5. Sales & Fulfillment KPIs

---

## Orders by Status

Track:

- Draft
- Confirmed
- Picking
- Delivered
- Cancelled

---

## Perfect Order Rate

### Formula

```
Perfect Orders
--------------
Total Orders
×100
```

A perfect order is delivered:

- On time
- Complete
- Damage free
- Correct documentation

---

## Order Cycle Time

### Formula

```
Delivery Date
-
Order Date
```

---

## Backorders

Customer orders waiting for inventory availability.

---

## Cancellation Rate

### Formula

```
Cancelled Orders
----------------
Total Orders
×100
```

---

# 6. Logistics KPIs

---

## Shipment Count

Total shipments completed.

---

## Average Delivery Time

### Formula

```
Delivery Date
-
Shipment Date
```

---

## Transportation Cost

Total logistics expenses.

---

## Carrier Performance

Evaluated using:

- On-time delivery
- Delivery accuracy
- Damage rate

---

## Delivery Delay

### Formula

```
Actual Delivery Date
-
Expected Delivery Date
```

---

# 7. Returns & Quality KPIs

---

## Return Rate

### Formula

```
Returned Orders
---------------
Delivered Orders
×100
```

---

## Product Defect Rate

### Formula

```
Defective Items
---------------
Delivered Items
×100
```

---

## Supplier Quality Issues

Number of rejected products received from suppliers.

---

## Return Reasons

Examples include:

- Damaged Product
- Wrong Product
- Customer Changed Mind
- Quality Issue
- Shipping Damage

---

# KPI Refresh Schedule

| KPI Category | Refresh Frequency |
|--------------|------------------|
| Executive | Daily |
| Procurement | Daily |
| Inventory | Daily |
| Warehouse | Daily |
| Sales | Daily |
| Logistics | Daily |
| Returns | Daily |

---

# KPI Ownership

| Department | KPI Owner |
|------------|-----------|
| Executive | CEO |
| Procurement | Procurement Manager |
| Inventory | Inventory Manager |
| Warehouse | Warehouse Manager |
| Logistics | Logistics Manager |
| Sales | Sales Manager |
| Returns | Quality Manager |
| Technical | Data Engineering Team |

---

# Business Impact

These KPIs enable the organization to:

- Monitor supply chain performance.
- Improve procurement decisions.
- Reduce stockouts and overstock.
- Optimize warehouse utilization.
- Improve delivery performance.
- Increase customer satisfaction.
- Support executive decision-making with trusted data.

---

# Phase 1 Summary

Phase 1 established the business foundation for the Supply Chain Intelligence Platform by defining:

- Business objectives
- Business requirements
- Stakeholders
- Supply chain process
- KPI framework

These documents will guide the remaining phases of the project, ensuring that every technical component directly supports business goals.

---

# Next Phase

Phase 2 – Data Source Identification

The next phase focuses on analyzing the ERPNext data model, identifying required DocTypes, mapping REST API endpoints, defining source-to-target mappings, and planning the data extraction strategy for the ETL pipeline.