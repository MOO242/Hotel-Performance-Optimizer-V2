# **1. Descriptive Analytics**

## **What happened? (Historical Reporting)**

---

## **📈 Revenue Performance**

### **4. What was the Occupancy trend over time?**

```sql
select
    c.year_number,
    SUM(a.rooms_sold) / SUM(a.rooms_available) * 100 as occupancy_rate,
    ROUND(
        (
            SUM(a.rooms_sold) / SUM(a.rooms_available) - LAG(SUM(a.rooms_sold) / SUM(a.rooms_available)) OVER(
                ORDER BY
                    C.YEAR_NUMBER
            )
        ) / LAG(SUM(a.rooms_sold) / SUM(a.rooms_available)) OVER(
            ORDER BY
                C.YEAR_NUMBER
        ) * 100,
        2
    ) AS YOY_GROWTH_PCT
FROM
    HPOV2_DB.ANALYTICS.FACT_ROOM_INVENTORY AS a
    JOIN HPOV2_DB.ANALYTICS.DIM_DATE AS c ON c.date_key = a.date_key
GROUP BY
    c.year_number
ORDER BY
    c.year_number;
```

## Result

2023 = % 68.57
2024 = % 68.60 YoY = %0.04
2025 = % 68.64 YoY = %0.07

---

### 🧠 Business Insight

Occupancy remained essentially flat across the portfolio, from 68.57% in 2023 to 68.64% in 2025 (+0.04% in 2024, +0.06% in 2025). Unlike revenue, RevPAR, and ADR — which grew strongly in 2024 before decelerating — occupancy shows no meaningful movement in either direction across the full period.

Combined with ADR's continued growth, this suggests 2025's revenue slowdown was not driven by falling demand (occupancy held steady) but more likely by a ceiling on pricing power or a shift in booking mix. Phase 3 diagnostic analysis should test this directly.ng.

### 🎯 Recommendation

Focus on identifying opportunities to increase occupancy while maintaining current pricing strength by analyzing:

- Underperforming properties
- Market segments with low occupancy
- Booking channel effectiveness
- Seasonal demand patterns
- Geographic demand trends

Since ADR is already improving, increasing occupancy without materially reducing room rates could generate additional RevPAR growth.

This will help identify which factors contributed most to the low occupancy levels and where corrective actions should be focused.

### 💼 Business Impact

Occupancy measures how effectively available room inventory is utilized.

Maintaining occupancy above 68% while improving ADR demonstrates healthy commercial performance and supports sustainable revenue growth. Further occupancy improvements can increase revenue without requiring additional room inventory, helping maximize asset utilization and profitability.
---
