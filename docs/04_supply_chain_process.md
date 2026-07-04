# Supply Chain Business Process

## Project

Supply Chain Intelligence Platform

---

# Purpose

This document describes the end-to-end business process followed by the organization, from supplier procurement to customer delivery and product returns.

Understanding the complete supply chain workflow helps identify:

- Business entities
- ERPNext modules
- API endpoints
- Database tables
- Relationships
- KPIs
- ETL requirements

This process serves as the foundation for the data engineering pipeline and analytics warehouse.

---

# End-to-End Supply Chain Process

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
Supplier Delivery
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
Customer Sales Order
    │
    ▼
Pick & Pack
    │
    ▼
Delivery Note
    │
    ▼
Shipment
    │
    ▼
Customer
    │
    ▼
Return / Replacement
```

---

# Business Process Flow

## Step 1 – Supplier Management

The procurement team identifies suppliers capable of providing products required by the business.

### Objectives

- Maintain supplier information
- Evaluate supplier performance
- Track supplier lead time

### ERPNext Module

Supplier

### Outputs

- Supplier Master
- Supplier Contact Information
- Supplier Category

---

## Step 2 – Purchase Requisition

Business departments identify inventory requirements and raise purchase requests.

### Objectives

- Identify stock requirements
- Prevent stock shortages

### ERPNext Module

Material Request

### Outputs

- Requested Products
- Requested Quantity
- Required Date

---

## Step 3 – Purchase Order

The procurement team creates a purchase order and sends it to the selected supplier.

### Objectives

- Purchase inventory
- Track procurement spending
- Monitor supplier commitments

### ERPNext Module

Purchase Order

### Outputs

- Purchase Order Number
- Supplier
- Ordered Quantity
- Expected Delivery Date

---

## Step 4 – Supplier Delivery

The supplier ships goods to the warehouse according to the purchase order.

### Objectives

- Monitor supplier delivery
- Compare expected vs actual delivery

### Outputs

- Shipment Date
- Delivery Status
- Lead Time

---

## Step 5 – Purchase Receipt

Warehouse staff verify received goods before adding inventory to stock.

### Objectives

- Validate received quantity
- Detect damaged goods
- Update inventory

### ERPNext Module

Purchase Receipt

### Outputs

- Received Quantity
- Accepted Quantity
- Rejected Quantity

---

## Step 6 – Warehouse Inventory

Approved inventory is stored inside warehouses.

### Objectives

- Track inventory
- Monitor warehouse capacity
- Maintain inventory accuracy

### ERPNext Modules

- Warehouse
- Item
- Bin

### Outputs

- Current Stock
- Inventory Value
- Warehouse Utilization

---

## Step 7 – Inventory Movement

Inventory moves between warehouses or storage locations as operational needs change.

### Objectives

- Track inventory movement
- Maintain stock accuracy

### ERPNext Module

Stock Entry

### Outputs

- Source Warehouse
- Destination Warehouse
- Quantity Moved
- Movement Type

---

## Step 8 – Customer Sales Order

Customers place purchase orders through retail or online channels.

### Objectives

- Record customer demand
- Allocate inventory
- Track order lifecycle

### ERPNext Module

Sales Order

### Outputs

- Sales Order
- Customer
- Ordered Items
- Order Status

---

## Step 9 – Pick & Pack

Warehouse employees prepare products for shipment.

### Objectives

- Reduce fulfillment time
- Ensure order accuracy

### Outputs

- Picked Quantity
- Packed Quantity
- Ready for Shipment

---

## Step 10 – Delivery Note

Products are dispatched to customers.

### Objectives

- Record shipments
- Update inventory
- Monitor fulfillment

### ERPNext Module

Delivery Note

### Outputs

- Delivery Date
- Delivered Quantity
- Shipment Status

---

## Step 11 – Shipment

Logistics providers transport products to customers.

### Objectives

- Improve delivery performance
- Reduce transportation cost

### Outputs

- Carrier
- Tracking Number
- Delivery Time
- Transportation Cost

---

## Step 12 – Customer Delivery

Customers receive products.

### Objectives

- Complete order fulfillment
- Improve customer satisfaction

### Outputs

- Delivery Confirmation
- Delivery Date
- Customer Feedback

---

## Step 13 – Returns

Customers return defective or unwanted products.

### Objectives

- Improve product quality
- Reduce return rate
- Analyze return reasons

### ERPNext Modules

- Sales Return
- Stock Entry

### Outputs

- Return Quantity
- Return Reason
- Replacement Status

---

# ERPNext Modules Used

| Business Process | ERPNext Module |
|------------------|----------------|
| Supplier Management | Supplier |
| Purchase Request | Material Request |
| Purchase Order | Purchase Order |
| Goods Receipt | Purchase Receipt |
| Product Master | Item |
| Inventory | Bin |
| Warehouse | Warehouse |
| Inventory Movement | Stock Entry |
| Customer Orders | Sales Order |
| Delivery | Delivery Note |
| Customer | Customer |

---

# Data Flow

```text
ERPNext
      │
      ▼
REST APIs
      │
      ▼
Python ETL
      │
      ▼
PostgreSQL Bronze Layer
      │
      ▼
Data Validation
      │
      ▼
Silver Layer
      │
      ▼
dbt Transformations
      │
      ▼
Gold Layer
      │
      ▼
Power BI Dashboards
```

---

# Business Events Captured

The analytics platform will capture the following business events:

- Supplier Created
- Purchase Order Issued
- Goods Received
- Inventory Updated
- Stock Transferred
- Customer Order Created
- Order Shipped
- Order Delivered
- Product Returned

These events will form the basis for historical reporting and KPI calculations.

---

# Key Business Metrics Generated

The business process supports calculation of:

## Procurement

- Purchase Cycle Time
- Supplier Lead Time
- Supplier Spend
- Supplier Performance

## Inventory

- Inventory Value
- Inventory Turnover
- Stockout Rate
- Overstock
- Dead Stock

## Warehouse

- Warehouse Utilization
- Inventory by Warehouse
- Stock Movements

## Sales

- Order Fulfillment Rate
- Perfect Order Rate
- Backorders
- Order Cycle Time

## Logistics

- Shipment Count
- On-Time Delivery
- Transportation Cost
- Carrier Performance

## Returns

- Return Rate
- Product Defect Rate
- Supplier Quality Issues

---

# Business Process Summary

The supply chain begins with procurement from suppliers, continues through inventory storage and warehouse operations, fulfills customer orders through logistics, and concludes with delivery and returns.

Every stage generates operational data that will be extracted from ERPNext, transformed into analytics-ready datasets, and visualized through Power BI dashboards.

This process map provides the business foundation for designing the ETL pipeline, data warehouse, and KPI framework.

---

# Next Document

The next document is **05_kpi_definitions.md**, where every KPI used in the dashboards will be formally defined, including its business purpose, calculation formula, interpretation, and required data sources.