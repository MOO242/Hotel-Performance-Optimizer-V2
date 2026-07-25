# **1. Descriptive Analytics**

## **What happened? (Historical Reporting)**

---

## **📈 Booking Performance**

### 11- What were the peak booking periods?

```sql
SELECT
    b.month,
    b.year_number,
    sum(a.room_revenue) total_revenue,
    COUNT(*) AS total_bookings
FROM
    HPOV2_DB.ANALYTICS.FACT_RESERVATIONS AS a
    LEFT JOIN HPOV2_DB.ANALYTICS.DIM_DATE AS b ON A.BOOKING_DATE_KEY = B.DATE_KEY
GROUP BY
    b.month,
    b.year_number
ORDER BY
    total_revenue DESC;


```

### 🧠 Business Insight

Top booking periods appear to be:

| Year | Month | Bookings | Revenue |
| ---- | ----- | -------: | ------: |
| 2025 | 7     |   14,573 |  11.21M |
| 2024 | 10    |   14,403 |  11.20M |
| 2023 | 8     |   14,292 |  11.15M |
| 2023 | 3     |   14,278 |  11.14M |
| 2025 | 1     |   14,467 |  11.10M |

- Booking volume is relatively consistent across top periods (14K-15K bookings).
- July 2025 shows the highest booking volume.
- October 2024 generated almost the same revenue with fewer bookings. Plus, October 2024 achieved similar revenue with fewer bookings, suggesting a stronger ADR and potentially a more profitable booking mix than July 2025.

### Recommendation

Analyze ADR, RevPAR, market segments, and booking channels for October 2024 to identify revenue optimization opportunities that can be replicated during other high-demand periods.

### Business Impact

Replicating the pricing and segment mix observed in October 2024 could improve revenue performance without requiring a significant increase in booking volume.

---
