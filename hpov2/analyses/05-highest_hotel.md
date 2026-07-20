# **1. Descriptive Analytics**

## **What happened? (Historical Reporting)**

---

## **📈 Revenue Performance**

### **5. Which hotels generated the highest revenue?**

```sql
With revenue_by_year as (
    SELECT
        c.year_number,
        b.property_name,
        sum(a.total_revenue) as total_revenue
    from
        HPOV2_DB.ANALYTICS.FACT_RESERVATIONS as a
        LEFT JOIN HPOV2_DB.ANALYTICS.DIM_DATE as c ON c.DATE_KEY = a.booking_date_key
        LEFT JOIN HPOV2_DB.ANALYTICS.DIM_HOTELS as b ON b.property_id = a.property_id
    group by
        c.year_number,
        b.property_name
)
SELECT
    year_number,
    property_name,
    total_revenue,
    rank () over (
        partition by year_number
        order by
            total_revenue DESC
    ) as revenue_rank
from
    revenue_by_year

order by
    year_number,
    revenue_rank;


```

---

### 🧠 Business Insight

Solaria House Barcelona was the highest revenue-generating property across all three years analyzed.

2023: $39.30M
2024: $40.52M
2025: $37.37M

The property consistently ranked as the portfolio's top revenue contributor, demonstrating strong commercial performance and sustained demand. Revenue peaked in 2024, before declining slightly in 2025, which may indicate changes in occupancy, pricing strategy, market demand, competitive pressures, or booking mix.
Despite the decline in 2025, Solaria House Barcelona remained the strongest-performing hotel in the portfolio, highlighting its importance to overall revenue generation.

### 🎯 Recommendation

Perform a deeper analysis of Solaria House Barcelona to understand the drivers of its success:

Compare ADR, Occupancy, and RevPAR against the portfolio average.
Analyze booking channel contribution.
Review market segment mix.
Investigate seasonal revenue patterns.
Compare 2024 and 2025 performance to identify causes of the revenue decline.

Additionally, identify best practices from this property that could be applied to lower-performing hotels across the portfolio.

### 💼 Business Impact

Understanding why Solaria House Barcelona consistently outperformed other properties enables commercial teams to:

Replicate successful revenue management strategies.
Improve pricing and distribution decisions.
Benchmark property performance.
Identify growth opportunities across the portfolio.
Enhance overall revenue and profitability.

---
