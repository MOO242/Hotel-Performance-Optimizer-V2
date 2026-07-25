# **1. Descriptive Analytics**

## **What happened? (Historical Reporting)**

---

## **📈 Guest Behavior**

### 15 - What was the average number of bookings per customer ?

```sql
SELECT
    AVG(booking_count) AS avg_bookings_per_customer
FROM (
    SELECT
        customer_id,
        COUNT(*) AS booking_count
    FROM HPOV2_DB.ANALYTICS.FACT_RESERVATIONS
    GROUP BY customer_id
)

```

## Business Insight

- Customers generate multiple reservations over time.
- The customer base contributes recurring business.
- Guest retention and repeat booking behavior may be significant drivers of demand.

## Recommendation

Identify high-frequency customers and analyze:

- Revenue contribution
- Booking channels
- Market segments
- Length of stay
- Cancellation behavior

## Business Impact

Understanding repeat booking behavior can support:

- Loyalty program optimization
- Customer retention strategies
- Targeted marketing campaigns
- Lifetime value analysis

---
