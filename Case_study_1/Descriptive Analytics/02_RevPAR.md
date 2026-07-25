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
        SUM(ROOM_REVENUE) AS ROOM_REVENUE
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
    sum(a.ROOM_REVENUE) / sum(b.rooms_available) as RevPAR,
    ROUND (
        (
            sum(a.ROOM_REVENUE) / sum(b.rooms_available) - LAG(
                sum(a.ROOM_REVENUE) / sum(b.rooms_available)) OVER(
                    ORDER BY
                        c.year_number
                )
            ) / LAG(
                sum(a.ROOM_REVENUE) / sum(b.rooms_available))  OVER(
                    ORDER BY
                        c.year_number
                ) * 100,
                2
            ) AS YOY_GROWTH_PCT
        FROM
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

2023 = $ 16.24
2024 = $ 16.72 YoY = 3.01 %
2025 = $ 16.84 YoY = 0.68 %

---

### **🧠 Business Insight**

---

RevPAR increased from $16.24 in 2023 to $16.84 in 2025, growing 2.96% in 2024 before nearly stalling at 0.68% in 2025 — consistent with the deceleration seen in total room revenue.

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
