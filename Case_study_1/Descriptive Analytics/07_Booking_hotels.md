# **1. Descriptive Analytics**

## **What happened? (Historical Reporting)**

---

## **📈 Booking Performance**

### **7 -How many bookings were received ?**

```sql
SELECT
    b.year_number,
    (COUNT (booking_id)) AS total_bookings
from
    HPOV2_DB.ANALYTICS.FACT_RESERVATIONS as a
    left join HPOV2_DB.ANALYTICS.DIM_DATE as b on b.date_key = a.check_in_date_key
group by
    b.year_number;
---

### 🧠 Business Insight

YoY Change

2024 vs 2023: +12,210 bookings (+7.6%)
2025 vs 2024: -5,719 bookings (-3.3%)

Total reservations across the portfolio increased from 160,433 bookings in 2023 to 172,643 bookings in 2024 (+7.6%), indicating strong growth in customer demand.
However, booking volume declined to 166,924 bookings in 2025 (-3.3%), suggesting a slowdown in demand generation or conversion performance across the portfolio.
This decline warrants further investigation to determine whether reduced booking activity was driven by:

Lower occupancy demand
ADR pricing changes
Reduced inventory availability
Shift in booking channel performance
Market segment weakness
Economic or competitive market factors
Changes in seasonality or travel patterns

### 🎯 Recommendation

Perform a deeper portfolio analysis focusing on:

**Demand Metrics**
- Occupancy %
- Rooms Sold
- Market Share

**Revenue Metrics**
- ADR
- RevPAR
- Total Revenue

**Commercial Performance**
- Booking Channel Mix
- Market Segment Contribution
- Lead Time
- Length of Stay (LOS)

**Trend Analysis**
- Monthly Booking Trends
- Seasonal Patterns
- Property Performance Comparison
- Year-over-Year Performance by Hotel

The objective is to identify whether the booking decline is demand-related, pricing-related, inventory-related, or caused by commercial execution challenges.

### 💼 Business Impact

Understanding the drivers behind the 2025 booking decline enables commercial leaders to:

- Protect future revenue performance
- Improve demand generation strategies
- Optimize sales and marketing investment
- Refine pricing and revenue management decisions
- Identify underperforming properties and segments
- Increase occupancy and market share
- Improve portfolio forecasting accuracy

Even a modest recovery of the lost 5,719 bookings could generate significant incremental revenue and strengthen overall portfolio performance.e.
```
