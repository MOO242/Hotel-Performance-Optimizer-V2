# **1. Descriptive Analytics**

## **What happened? (Historical Reporting)**

---

## **📈 Guest Behavior**

### 12- What was the average Booking Lead Time?

```sql
SELECT
    AVG (
        DATEDIFF(
            DAY,
            to_date(
                TO_VARCHAR(booking_date_key),
                'YYYYMMDD'
            ),
            to_date(
                TO_VARCHAR(check_in_date_key),
                'YYYYMMDD'
            )
        )
    ) AS Lead_time
FROM
    HPOV2_DB.ANALYTICS.FACT_RESERVATIONS


```

### 🧠 Business Insight

Average Booking Lead Time = 15.28 Days

Guests book approx 15 days before arrival on average. This indicates relatively short booking windows, suggest that increasing pricing, as demand forecasting got increased within 0-30 days before arrival days and monitor booking pace.

### Key Insights

Revenue Management should closely monitor booking pace within the 30-day arrival window and adjust pricing dynamically to capture short-term demand opportunities.

### Recommendation

Understanding booking lead time improves occupancy forecasting accuracy, supports more effective pricing decisions, and helps identify opportunities for targeted promotional campaigns.

---
