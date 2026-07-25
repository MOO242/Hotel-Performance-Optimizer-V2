# **1. Descriptive Analytics**

## **What happened? (Historical Reporting)**

---

## **📈 Guest Behavior**

### 14- What was the Cancellation Rate?

```sql
SELECT
    COUNT(CASE WHEN booking_status = 'Cancelled' THEN 1 END) * 100.0 / COUNT(booking_id) AS cancellation_rate
FROM
    HPOV2_DB.ANALYTICS.FACT_RESERVATIONS


```

## Business Insight

Approximately 19.94% of all reservations were cancelled, meaning nearly 1 in every 5 bookings did not materialize into a stay. This represents a significant source of revenue leakage and forecasting uncertainty.

## Recommendation

Analyze cancellation behavior by:

Booking Channel
Market Segment
Hotel
Lead Time Bucket
Room Type

to identify the primary drivers of cancellations.

## Business Impact

Reducing the cancellation rate from 19.94% to 17.94% could significantly improve occupancy performance, forecasting accuracy, and realized room revenue.

---
