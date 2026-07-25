# **1. Descriptive Analytics**

## **What happened? (Historical Reporting)**

---

## **📈 Revenue Performance**

### **5. Which hotels generated the highest gross booking value?**

```sql
WITH revenue_by_year AS (
    SELECT
        c.year_number,
        b.property_name,
        SUM(a.total_revenue) AS total_revenue
    FROM
        HPOV2_DB.ANALYTICS.FACT_RESERVATIONS AS a
        LEFT JOIN HPOV2_DB.ANALYTICS.DIM_DATE AS c ON c.DATE_KEY = a.booking_date_key
        LEFT JOIN HPOV2_DB.ANALYTICS.DIM_HOTELS AS b ON b.property_id = a.property_id
    GROUP BY
        c.year_number,
        b.property_name
)
SELECT
    year_number,
    property_name,
    total_revenue,
    RANK() OVER (
        PARTITION BY year_number
        ORDER BY total_revenue DESC
    ) AS revenue_rank
FROM
    revenue_by_year
ORDER BY
    year_number,
    revenue_rank;
```

_Note: figures reflect total booking value by booking date, across all booking statuses (not limited to Checked Out) — not directly comparable to the room-revenue figures earlier in this document._

### 🧠 Business Insight

Solaria House Barcelona was the top property by gross booking value across all three years — and consistently surfaced as the top result across every property-level query run so far, not just this one.

2023: $39.30M
2024: $40.52M
2025: $37.37M

Booking value grew 3.1% in 2024 before dropping 7.8% in 2025 — a sharper reversal than the portfolio-wide deceleration seen in the aggregate KPIs, and a net decline of 4.9% since 2023.

### 🎯 Recommendation

Perform a deeper analysis of Solaria House Barcelona to understand the drivers behind both its consistent top ranking and its 2025 reversal:

- Compare ADR, Occupancy, and RevPAR against the portfolio average
- Analyze booking channel contribution
- Review market segment mix
- Investigate seasonal revenue patterns
- Compare 2024 and 2025 performance to identify causes of the decline

Additionally, identify best practices from this property that could be applied to lower-performing hotels across the portfolio.

### 💼 Business Impact

Understanding why Solaria House Barcelona consistently outperformed other properties — and why that performance reversed in 2025 — enables commercial teams to:

- Replicate successful revenue management strategies
- Improve pricing and distribution decisions
- Benchmark property performance
- Identify growth opportunities across the portfolio
- Enhance overall revenue and profitability
