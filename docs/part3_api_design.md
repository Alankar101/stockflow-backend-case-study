# Part 3: Low-Stock Alert API Design

## Endpoint
GET /api/companies/{company_id}/alerts/low-stock

---

## Business Rules Implemented

- Low stock threshold varies by product
- Alerts generated only if recent sales activity exists
- Multiple warehouses supported
- Supplier information included for reordering

---

## Assumptions

- Recent sales = sales in the last 30 days
- Sales data is derived from an assumed orders table
- One primary supplier per product
- Alerts are generated per warehouse

---

## Logic Flow

1. Fetch inventory records for the given company
2. Check if inventory quantity is below threshold
3. Verify recent sales activity
4. Calculate daily usage and estimated stock-out days
5. Attach supplier details
6. Return structured alert response

---

## Edge Cases Handled

- No recent sales → no alert
- Zero daily usage → avoid division errors
- Products stored in multiple warehouses
- Missing supplier data handled gracefully

---

## Why This Design

- Keeps API response business-focused
- Avoids unnecessary alerts
- Scales well with additional warehouses
- Aligns with real-world inventory workflows

---

## Future Improvements

- Add pagination for alerts
- Include priority levels for alerts
- Support configurable sales windows
- Cache frequent alert calculations
