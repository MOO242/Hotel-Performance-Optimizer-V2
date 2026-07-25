# **1. Descriptive Analytics**

## **What happened? (Historical Reporting)**

---

## **📈 Booking Performance**

### **8 -Which booking channels generated the most reservations ?**

```sql
SELECT
    a.booking_channel,
    (COUNT(a.booking_id)) as total_reservation
FROM
    HPOV2_DB.ANALYTICS.FACT_RESERVATIONS as a
GROUP BY
    a.booking_channel
ORDER BY
    a.booking_channel DESC;
```

---

### 🧠 Business Insight

| Booking Channel       | Reservations |
| --------------------- | -----------: |
| Velora.com            |       89,496 |
| OTA - Booking.com     |       80,427 |
| Property Direct       |       75,304 |
| OTA - Expedia         |       69,800 |
| Corporate Travel Desk |       54,985 |
| Velora App            |       45,227 |
| Travel Agent          |       45,036 |
| GDS - Corporate       |       39,725 |

Booking demand was primarily driven by direct digital channels, with **Velora.com generating the highest reservation volume (89,496 bookings)** across the portfolio.

Among third-party distribution channels, **OTA - Booking.com (80,427 bookings)** and **OTA - Expedia (69,800 bookings)** were significant contributors, collectively generating substantial demand and highlighting the portfolio's reliance on online travel agencies.

**Property Direct bookings (75,304)** also represented a strong source of demand, demonstrating the importance of hotel-level customer acquisition efforts.

Corporate-focused channels, including **Corporate Travel Desk** and **GDS - Corporate**, contributed a meaningful share of reservations, supporting business travel demand across the portfolio.

Overall, the booking mix indicates a balanced distribution strategy across direct, OTA, and corporate channels, although direct digital channels remain the largest source of reservation volume.

### 🎯 Recommendation

Evaluate channel performance beyond reservation volume by analyzing:

Total Revenue by Channel
ADR by Channel
RevPAR Contribution
Cancellation Rate
Average Length of Stay (LOS)
Market Segment Mix
Cost of Acquisition
Net Revenue After Distribution Costs

The objective is to determine whether high-volume channels are also the most profitable channels.

### 💼 Business Impact

Understanding channel contribution enables commercial leaders to:

Optimize channel mix and distribution strategy.
Increase direct bookings and reduce OTA dependency.
Improve marketing investment allocation.
Enhance revenue management decisions.
Identify the most profitable demand sources.
Increase overall portfolio revenue and profitability.

A shift of demand toward high-performing direct channels can improve profit margins while maintaining strong occupancy and revenue performance.
