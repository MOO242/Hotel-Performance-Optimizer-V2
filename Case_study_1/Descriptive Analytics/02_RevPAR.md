# **1. Descriptive Analytics**

## **What happened? (Historical Reporting)**

---

## **📈 Revenue Performance**

### **2. What was the RevPAR trend over time?**

Snowflake engine

```sql
WITH YEARLY_REVENUE AS (
    SELECT
        d.year_number,
        SUM(r.room_revenue) AS total_revenue
    FROM
        HPOV2_DB.ANALYTICS.FACT_RESERVATIONS r
        LEFT JOIN HPOV2_DB.ANALYTICS.DIM_DATE d ON r.check_in_date_key = d.date_key
    WHERE
        r.booking_status = 'Checked Out'
    GROUP BY
        d.year_number
),

YEARLY_ROOMS_AVAILABLE AS (
    SELECT
        d.year_number,
        SUM(i.rooms_available) AS total_rooms_available
    FROM
        HPOV2_DB.ANALYTICS.FACT_ROOM_INVENTORY i
        LEFT JOIN HPOV2_DB.ANALYTICS.DIM_DATE d ON i.date_key = d.date_key
    GROUP BY
        d.year_number
)

SELECT
    rev.year_number,
    rev.total_revenue / inv.total_rooms_available AS RevPAR,
    ROUND(
        (
            (rev.total_revenue / inv.total_rooms_available)
            - LAG(rev.total_revenue / inv.total_rooms_available) OVER (ORDER BY rev.year_number)
        )
        / LAG(rev.total_revenue / inv.total_rooms_available) OVER (ORDER BY rev.year_number)
        * 100,
        2
    ) AS YOY_GROWTH_PCT
FROM
    YEARLY_REVENUE rev
    JOIN YEARLY_ROOMS_AVAILABLE inv ON rev.year_number = inv.year_number
ORDER BY
    rev.year_number;



```

### **Result**

2023 = $ 15.47
2024 = $ 16.11 YoY = 4.17 %
2025 = $ 16.22 YoY = 0.68 %

---

### **🧠 Business Insight**

---

RevPAR increased from $15.468407 in 2023 to $16.222089 in 2025, growing 4.17% in 2024 before nearly stalling at 0.68% in 2025 — consistent with the deceleration seen in total room revenue.

This flags a need for deeper investigation into pricing strategy (ADR) and demand (occupancy) to understand what's driving the flattening.

### **🎯 Recommendation**

---

Perform a deeper analysis of the key RevPAR drivers:

- Analyze ADR trends to determine whether pricing contributed to growth.
- Analyze Occupancy trends to evaluate demand performance.
- Compare RevPAR by Property to identify top and bottom performers.
- Review Market Segment performance to understand revenue contribution.
- Evaluate Booking Channel effectiveness and profitability.
- Investigate properties with stagnant or declining RevPAR.

### **💼 Business Impact**

---

RevPAR is one of the most important hotel performance KPIs because it measures how effectively available room inventory is converted into revenue.

Improving RevPAR can:

- Increase revenue efficiency.
- Improve hotel profitability.
- Support better pricing decisions.
- Identify underperforming properties.
- Guide commercial investment and sales strategies.

Higher RevPAR generally indicates stronger overall commercial performance and more effective utilization of available room inventory.
