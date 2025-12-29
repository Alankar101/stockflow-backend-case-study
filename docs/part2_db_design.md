# Part 2: Database Design

## Overview
The database is designed to support:
- Multiple companies
- Multiple warehouses per company
- Products stored in multiple warehouses
- Inventory change tracking
- Supplier relationships
- Product bundles

---

## Tables & Relationships

### Company
- id (PK)
- name

### Warehouse
- id (PK)
- name
- company_id (FK → Company)

### Product
- id (PK)
- name
- sku (UNIQUE)
- low_stock_threshold

### Inventory
- id (PK)
- product_id (FK → Product)
- warehouse_id (FK → Warehouse)
- quantity

### Supplier
- id (PK)
- name
- contact_email

---

## Design Decisions

- Inventory is separated from Product to support multi-warehouse storage
- SKU uniqueness ensures platform-wide product identification
- Foreign keys maintain data integrity
- Low stock threshold stored at product level for flexibility

---

## Missing Requirements / Questions

1. Is SKU unique globally or per company?
2. Should low-stock alerts be per warehouse or aggregated?
3. How is sales activity tracked?
4. Can suppliers be shared across companies?
5. How should bundle inventory be calculated?

---

## Scalability Considerations

- Indexes on SKU and foreign keys
- Inventory table allows horizontal scaling
- Schema supports future extensions like sales and audit logs
