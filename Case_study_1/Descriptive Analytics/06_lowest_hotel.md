# **1. Descriptive Analytics**

## **What happened? (Historical Reporting)**

---

## **📈 Revenue Performance**

### **6. Which hotels generated the lowest revenue?**

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
        ORDER BY total_revenue ASC
    ) AS revenue_rank
FROM
    revenue_by_year
ORDER BY
    year_number,
    revenue_rank;
```

_Note: figures reflect total booking value by booking date, across all booking statuses — not directly comparable to the room-revenue figures earlier in this document._

### 🧠 Business Insight

The analysis identified the lowest revenue-generating properties within the portfolio across the reporting period.

2023: NovaPoint Dubai ($986,180.41)
2024: Cortina Inn Milan ($981,429.19)
2025: Cortina Inn Milan ($952,553.29)

These properties consistently generated substantially less revenue than their peers — roughly 40x less than Solaria House Barcelona, the portfolio's top performer — indicating potential challenges related to demand, pricing strategy, occupancy performance, market positioning, inventory size, or channel effectiveness.

Notably, Cortina Inn Milan was the lowest revenue-generating property in both 2024 and 2025, declining a further 2.9% year-over-year. This warrants investigation into whether the trend is driven by reduced demand, lower ADR, declining occupancy, competitive pressures, or operational constraints.

### 🎯 Recommendation

Conduct a detailed performance review of NovaPoint Dubai and Cortina Inn Milan by analyzing:

- Occupancy %
- ADR
- RevPAR
- Booking Channel Mix
- Market Segment Contribution
- Length of Stay
- Seasonal Demand Patterns
- Revenue Trend by Month
- Comparison against Portfolio Average

Determine whether the revenue performance gap is primarily driven by pricing, demand, market conditions, inventory limitations, or commercial strategy execution.

### 💼 Business Impact

Identifying low-performing properties enables commercial teams to:

- Prioritize revenue improvement initiatives
- Optimize pricing and revenue management strategies
- Increase occupancy through targeted sales and marketing efforts
- Benchmark properties against portfolio leaders
- Improve resource allocation and investment decisions
- Strengthen overall portfolio revenue performance

Addressing underperforming properties can unlock additional revenue opportunities and improve the portfolio's overall commercial effectiveness.
