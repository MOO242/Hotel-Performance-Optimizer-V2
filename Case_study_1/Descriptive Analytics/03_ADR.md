# **1. Descriptive Analytics**

## **What happened? (Historical Reporting)**

---

## **📈 Revenue Performance**

### **3. What was the ADR trend over time?**

```sql
WITH REVENUE_BY_DAY AS (
    SELECT
        property_id,
        CHECK_IN_DATE_KEY,
        SUM(ROOM_REVENUE) AS ROOM_REVENUE
    FROM
        HPOV2_DB.ANALYTICS.FACT_RESERVATIONS
    WHERE
        booking_status = 'Checked Out'
    GROUP BY
        property_id,
        CHECK_IN_DATE_KEY
)
SELECT
    c.year_number,
    SUM(a.ROOM_REVENUE) / SUM(b.rooms_sold) AS ADR,
    ROUND(
        (SUM(a.ROOM_REVENUE) / SUM(b.rooms_sold) - LAG(SUM(a.ROOM_REVENUE) / SUM(b.rooms_sold)) OVER (ORDER BY c.year_number))
        / LAG(SUM(a.ROOM_REVENUE) / SUM(b.rooms_sold)) OVER (ORDER BY c.year_number) * 100,
        2
    ) AS YOY_GROWTH_PCT
FROM
    REVENUE_BY_DAY AS a
    LEFT JOIN HPOV2_DB.ANALYTICS.FACT_ROOM_INVENTORY AS b ON a.property_id = b.property_id
    AND a.check_in_date_key = b.DATE_KEY
    LEFT JOIN HPOV2_DB.ANALYTICS.DIM_DATE AS c ON a.check_in_date_key = c.date_key
GROUP BY
    c.year_number
ORDER BY
    c.year_number;

```

## Result

2023 = $ 23.69
2024 = $ 24.37 YoY = 2.87%
2025 = $ 24.52 YoY = 0.62%

---

### **🧠 Business Insight**

---

ADR increased from $23.69 in 2023 to $24.52 in 2025, representing a 3.50% increase over the period.

This flags a need for deeper investigation into pricing strategy and demand (occupancy) to understand what's driving the flattening.

### **🎯 Recommendation**

---

Conduct deeper analysis to identify the primary drivers behind ADR growth by examining:

- Property-level ADR performance
- Market Segment ADR contribution
- Booking Channel profitability
- Room Type pricing trends
- Geographic market performance
- Seasonal pricing patterns

Identify the properties, segments, and channels that delivered the highest ADR growth and replicate successful pricing and revenue management strategies across underperforming hotels where appropriate.

### **💼 Business Impact**

---

ADR is a critical revenue management KPI because it measures the average revenue earned from each occupied room.

Improving ADR can:

- Increase room revenue without requiring additional occupancy
- Enhance overall hotel profitability
- Improve commercial performance
- Support more effective pricing decisions
- Strengthen revenue optimization strategies

When combined with stable or growing occupancy levels, higher ADR contributes directly to stronger revenue growth and improved financial performance.
