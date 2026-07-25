# **1. Descriptive Analytics**

## **What happened? (Historical Reporting)**

---

## **📈 Booking Performance**

### **10 - Which room types had the highest demand ?**

```sql

SELECT
    a.room_id,
    b.room_class,
    SUM (a.room_revenue) as total_revenue,
    ROUND (
        SUM(ROOM_REVENUE) * 100 / SUM(SUM(ROOM_REVENUE)) OVER(),
        2
    ) AS revenue_pct
FROM
    HPOV2_DB.ANALYTICS.FACT_RESERVATIONS AS a
    LEFT JOIN HPOV2_DB.ANALYTICS.DIM_ROOMS AS b ON a.room_id = b.room_id
GROUP BY
    a.room_id,
    b.room_class
ORDER by
    total_revenue DESC;

```

### 🧠 Business Insight

## Room Type Performance Analysis

| Room Type Code | Room Type Name     |   Room Revenue | Revenue Contribution (%) |
| -------------- | ------------------ | -------------: | -----------------------: |
| RT8            | Presidential Suite | 134,195,287.37 |                   35.18% |
| RT7            | Executive Suite    |  68,778,703.85 |                   18.03% |
| RT6            | Junior Suite       |  49,119,404.89 |                   12.88% |
| RT5            | Executive          |  38,811,339.63 |                   10.18% |
| RT4            | Club               |  30,846,138.54 |                    8.09% |
| RT3            | Deluxe             |  25,469,231.52 |                    6.68% |
| RT2            | Superior           |  19,363,582.40 |                    5.08% |
| RT1            | Standard           |  14,853,069.94 |                    3.89% |

- Presidential Suite (RT8) generated the highest revenue contribution at **35.18%**.
- Executive Suite (RT7) contributed **18.03%** of total revenue.
- Premium room categories (RT8, RT7, RT6) account for approximately **66.09%** of total room revenue.
- Standard and Superior room categories together contribute only **8.97%** of total revenue.
- Revenue is heavily concentrated in higher-tier room categories, indicating that suite inventory is a significant driver of hotel revenue performance.

### Recommendation

- Focus on upselling initiatives for Executive Suite, Junior Suite, and Presidential Suite categories.
- Review pricing strategies for lower-tier room categories to improve revenue contribution.
- Analyze occupancy and demand patterns for suite categories to maximize ADR and RevPAR.
- Consider targeted promotions that encourage upgrades from Standard and Superior rooms to premium room categories.

### Business Impact

- Increased suite upgrade conversion rates.
- Higher ADR and RevPAR performance.
- Improved revenue optimization across room inventory.
- Better understanding of room-type revenue concentration risk.
