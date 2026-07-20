# **1. Descriptive Analytics**

## **What happened? (Historical Reporting)**

---

## **📈 Revenue Performance**

### **4. What was the ADR trend over time?**

```sql
select
    c.year_number,
    sum(a.rooms_sold) / sum(a.rooms_available) * 100 as occupancy_rate
from
    HPOV2_DB.ANALYTICS.FACT_ROOM_INVENTORY AS a
join hpov2_db.analytics.dim_date as c
    on c.date_key = a.date_key


 group by
    c.year_number;

```

## Result

2023 = % 68.60
2024 = % 68.64
2025 = % 68.57

---

### 🧠 Business Insight

Occupancy remained stable across the portfolio between 2023 and 2025, increasing slightly from 68.57% to 68.64%.
The minimal change in occupancy indicates that room demand remained relatively consistent over the period. Since occupancy was largely unchanged while both ADR and RevPAR increased, revenue growth appears to have been driven primarily by improved pricing performance rather than significant increases in room demand.
This suggests that revenue management and pricing strategies were more influential than occupancy growth in driving overall revenue performance.

### 🎯 Recommendation

Focus on identifying opportunities to increase occupancy while maintaining current pricing strength by analyzing:

Underperforming properties
Market segments with low occupancy
Booking channel effectiveness
Seasonal demand patterns
Geographic demand trends

Since ADR is already improving, increasing occupancy without materially reducing room rates could generate additional RevPAR growth.

This will help identify which factors contributed most to the low occupancy levels and where corrective actions should be focused.

### 💼 Business Impact

Occupancy measures how effectively available room inventory is utilized.
Maintaining occupancy above 68% while improving ADR demonstrates healthy commercial performance and supports sustainable revenue growth. Further occupancy improvements can increase revenue without requiring additional room inventory, helping maximize asset utilization and profitability.

---
