# **1. Descriptive Analytics**

## **What happened? (Historical Reporting)**

---

## **📈 Revenue Performance**

### **1. What was the total Room Revenue?**

```sql
SELECT
    c.year_number,
    SUM(ROOM_REVENUE) as TOTAL_ROOM_REVENUE,
    ROUND (
        (
            SUM(a.ROOM_REVENUE) - lag(sum(a.ROOM_REVENUE)) over(
                order by
                    c.year_number
            )
        ) / lag(sum(a.ROOM_REVENUE)) over (
            order by
                c.year_number
        ) * 100,
        2
    ) as YOY_GROWTH_PCT
FROM
    HPOV2_DB.ANALYTICS.FACT_RESERVATIONS as a
    LEFT JOIN HPOV2_DB.ANALYTICS.DIM_DATE as c on a.check_in_date_key = c.date_key
WHERE
    booking_status = 'Checked Out'
group by
    c.year_number
ORDER BY
    c.year_number;
```

## Business Insight

The hotel portfolio demonstrated consistent year-over-year revenue growth across the three-year period.

2023: $118.05M
2024: $124.01M YoY = 5.05%
2025: $124.56M YoY = 0.44%

Total room revenue increased from $118.05M in 2023 to $124.56M in 2025, but growth was not evenly distributed across the period. Nearly all of the gain occurred between 2023 and 2024 (+5.05%), while 2025 growth nearly stalled at +0.44%.

The sharp deceleration in 2025 warrants further investigation — potential drivers include rate ceiling pressure, softening demand, increased competitive supply, or a shift in booking mix. Diagnostic analysis (Phase 3) will isolate which of these factors is responsible.

---

## Recommendation

Conduct deeper analysis to identify the key drivers behind the 2025 growth deceleration by examining:

- Property Performance
- Market Segment Performance
- Booking Channel Contribution
- Room Type Revenue
- ADR Trends
- Occupancy Trends
- RevPAR Trends

This analysis will help determine which factors contributed most to the slowdown and where commercial teams should focus investment and optimization efforts.

---

## Business Impact

Understanding the drivers behind the 2025 deceleration enables commercial leaders to:

- Optimize pricing and revenue management strategies
- Increase investment in high-performing channels and segments
- Prioritize top-performing properties
- Improve forecasting accuracy
- Support data-driven commercial decision making

These actions can help reverse the slowdown and restore stronger growth in 2026 and beyond.

---
