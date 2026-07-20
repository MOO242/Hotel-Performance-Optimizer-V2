# **1. Descriptive Analytics**

## **What happened? (Historical Reporting)**

---

## **📈 Revenue Performance**

### **1. What was the total Room Revenue?**

```sql
SELECT
    c.year_number,
    SUM(TOTAL_REVENUE) as TOTAL_REVENUE,
    ROUND (
        (
            SUM(a.TOTAL_REVENUE) - lag(sum(a.total_revenue)) over(
                order by
                    c.year_number
            )
        ) / lag(sum(a.total_revenue)) over (
            order by
                c.year_number
        ) * 100,
        2
    ) as YOY_GROWTH_PCT
FROM
    HPOV2_DB.ANALYTICS.FACT_RESERVATIONS as a
    LEFT JOIN HPOV2_DB.ANALYTICS.DIM_DATE as c on a.check_in_date_key = c.date_key
group by
    c.year_number
ORDER BY
    c.year_number;
```

### **🧠 Business Insight**

The hotel portfolio demonstrated consistent year-over-year revenue growth across the three-year period.

2023: $131.12M & NULL
2024: $136.86M & YOY_GROWTH = 44%
2025: $137.97M & YOY_GROWTH = 81%

Total room revenue increased from $131.12M in 2023 to $137.97M in 2025, indicating sustained business growth and healthy demand across the portfolio. The largest increase occurred between 2023 and 2024, while growth remained positive but slower in 2025.
This positive trend suggests that a combination of demand recovery, pricing strategy, occupancy improvements, or portfolio performance contributed to higher revenue generation over time

---

### **🎯 Recommendation**

Conduct deeper analysis to identify the key drivers behind revenue growth by examining:

Property Performance
Market Segment Performance
Booking Channel Contribution
Room Type Revenue
ADR Trends
Occupancy Trends
RevPAR Trends

This analysis will help determine which areas contributed most to revenue growth and where commercial teams should focus future investment and optimization efforts.e.

---

### **💼 Business Impact**

Understanding the drivers of revenue growth enables commercial leaders to:

Optimize pricing and revenue management strategies
Increase investment in high-performing channels and segments
Prioritize top-performing properties
Improve forecasting accuracy
Support data-driven commercial decision making

These actions can help maximize revenue opportunities and sustain portfolio growth in future periods, particularly throughout 2026 and beyond.

---
