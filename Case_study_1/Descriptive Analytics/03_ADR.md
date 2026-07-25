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
        SUM(TOTAL_REVENUE) AS total_revenue
    from
        HPOV2_DB.ANALYTICS.FACT_RESERVATIONS
    WHERE
        booking_status = 'Checked Out'
    group by
        property_id,
        CHECK_IN_DATE_KEY
)
SELECT
    c.year_number,
    sum(a.total_revenue) / sum(b.rooms_sold) as ADR
from
    REVENUE_BY_DAY as a
    LEFT JOIN HPOV2_DB.ANALYTICS.FACT_ROOM_INVENTORY as b on a.property_id = b.property_id
    AND a.check_in_date_key = b.DATE_KEY
    LEFT JOIN HPOV2_DB.ANALYTICS.DIM_DATE as c on a.check_in_date_key = c.date_key
group by
    c.year_number
order by
    c.year_number;

```

## Result

2023 = $ 25.27
2024 = $ 25.98
2025 = $ 26.17

---

### **🧠 Business Insight**

---

ADR increased from $25.27 in 2023 to $26.17 in 2025, representing a 3.56% increase over the period.
The steady growth in ADR indicates that the portfolio generated more revenue per occupied room over time. This suggests improved pricing effectiveness, stronger revenue management practices, a favorable room mix, or increased contribution from higher-value customer segments.
Although the growth rate is moderate, the consistent upward trend demonstrates positive pricing performance across the portfolio and contributed to overall revenue growth.

### **🎯 Recommendation**

---

Conduct deeper analysis to identify the primary drivers behind ADR growth by examining:

Property-level ADR performance
Market Segment ADR contribution
Booking Channel profitability
Room Type pricing trends
Geographic market performance
Seasonal pricing patterns

Identify the properties, segments, and channels that delivered the highest ADR growth and replicate successful pricing and revenue management strategies across underperforming hotels where appropriate.

### **💼 Business Impact**

---

ADR is a critical revenue management KPI because it measures the average revenue earned from each occupied room.
Improving ADR can:

Increase room revenue without requiring additional occupancy
Enhance overall hotel profitability
Improve commercial performance
Support more effective pricing decisions
Strengthen revenue optimization strategies

When combined with stable or growing occupancy levels, higher ADR contributes directly to stronger revenue growth and improved financial performance.