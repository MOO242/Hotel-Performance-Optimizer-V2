# **1. Descriptive Analytics**

## **What happened? (Historical Reporting)**

---

## **📈 Revenue Performance**

### **2. What was the RevPAR trend over time?**

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
    sum(a.total_revenue) / sum(b.rooms_available) as RevPAR
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

### **Result**

2023 = $ 17.32
2024 = $ 17.83
2025 = $ 17.97

---

### **🧠 Business Insight**

---

RevPAR increased from $17.32 in 2023 to $17.97 in 2025, representing approximately 3.75% growth over the period.
The consistent year-over-year increase suggests the portfolio generated more revenue from its available room inventory.

This improvement may be driven by stronger pricing performance (ADR), improved occupancy levels, or a combination of both factors.

While growth remains positive, the increase is relatively modest, indicating an opportunity to further optimize commercial strategies and maximize revenue potential across the portfolio.

### **🎯 Recommendation**

---

Perform a deeper analysis of the key RevPAR drivers:

Analyze ADR trends to determine whether pricing contributed to growth.
Analyze Occupancy trends to evaluate demand performance.
Compare RevPAR by Property to identify top and bottom performers.
Review Market Segment performance to understand revenue contribution.
Evaluate Booking Channel effectiveness and profitability.
Investigate properties with stagnant or declining RevPAR.

### **💼 Business Impact**

---

RevPAR is one of the most important hotel performance KPIs because it measures how effectively available room inventory is converted into revenue.
Improving RevPAR can:

Increase revenue efficiency.
Improve hotel profitability.
Support better pricing decisions.
Identify underperforming properties.
Guide commercial investment and sales strategies.

Higher RevPAR generally indicates stronger overall commercial performance and more effective utilization of available room inventory.
