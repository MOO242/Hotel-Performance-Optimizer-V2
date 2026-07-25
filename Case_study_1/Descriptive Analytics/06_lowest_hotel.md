# **1. Descriptive Analytics**

## **What happened? (Historical Reporting)**

---

## **📈 Revenue Performance**

### **6 - Which hotels generated the lowest revenue??**

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
            total_revenue ASC
    ) as revenue_rank
from
    revenue_by_year

order by
    year_number,
    revenue_rank;



```

---

### 🧠 Business Insight

The analysis identified the lowest revenue-generating properties within the portfolio across the reporting period.

2023: NovaPoint Dubai ($986,180.41)
2024: Cortina Inn Milan ($981,429.19)
2025: Cortina Inn Milan ($952,553.29)

These properties consistently generated substantially less revenue than their peers, indicating potential challenges related to demand, pricing strategy, occupancy performance, market positioning, inventory size, or channel effectiveness.
Notably, Cortina Inn Milan remained the lowest revenue-generating property for two consecutive years (2024 and 2025), while also experiencing a year-over-year revenue decline. This may warrant further investigation to determine whether the performance trend is driven by reduced demand, lower ADR, declining occupancy, competitive pressures, or operational constraints.

### 🎯 Recommendation

Conduct a detailed performance review of NovaPoint Dubai and Cortina Inn Milan by analyzing:

Occupancy %
ADR
RevPAR
Booking Channel Mix
Market Segment Contribution
Length of Stay
Seasonal Demand Patterns
Revenue Trend by Month
Comparison against Portfolio Average

Determine whether the revenue performance gap is primarily driven by pricing, demand, market conditions, inventory limitations, or commercial strategy execution.

### 💼 Business Impact

Identifying low-performing properties enables commercial teams to:

Prioritize revenue improvement initiatives.
Optimize pricing and revenue management strategies.
Increase occupancy through targeted sales and marketing efforts.
Benchmark properties against portfolio leaders.
Improve resource allocation and investment decisions.
Strengthen overall portfolio revenue performance.

Addressing underperforming properties can unlock additional revenue opportunities and improve the portfolio's overall commercial effectiveness.
