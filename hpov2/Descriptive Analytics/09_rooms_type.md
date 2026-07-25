# **1. Descriptive Analytics**

## **What happened? (Historical Reporting)**

---

## **📈 Booking Performance**

### **9 - Which market segments generated the most revenue ?**

```sql
SELECT
    a.market_segment,
    SUM(a.ROOM_REVENUE) AS TOTAL_REVENUE,
FROM
    HPOV2_DB.ANALYTICS.FACT_RESERVATIONS AS A
GROUP BY
    a.market_segment
ORDER BY
   SUM(a.ROOM_REVENUE) DESC;
```

### 🧠 Business Insight

| Market Segment | Reservations | Room Revenue |
| -------------- | -----------: | -----------: |
| Leisure        |      253,444 |     $193.17M |
| Corporate      |       94,710 |      $72.36M |
| Direct         |       84,108 |      $63.96M |
| OTA            |       45,340 |      $34.61M |
| Group          |       22,398 |      $17.33M |

Leisure travelers were the portfolio's largest source of demand, generating **253,444 reservations** and **$193.17M** in room revenue, accounting for approximately **50.6% of total revenue**. This indicates that leisure demand is the primary driver of both occupancy and revenue performance.

Corporate travelers contributed **94,710 reservations** and **$72.36M** in room revenue, making Corporate the second most valuable market segment.

Direct bookings generated **84,108 reservations** and **$63.96M** in room revenue, highlighting the effectiveness of direct customer acquisition efforts.

OTA channels delivered **45,340 reservations** and **$34.61M** in room revenue, while Group business generated **22,398 reservations** and **$17.33M** in room revenue.

Overall, the market segment mix shows a balanced portfolio supported by Leisure, Corporate, Direct, OTA, and Group demand. Leisure remains the dominant contributor to both reservations and revenue, while Corporate and Direct provide substantial revenue diversification.

### 🎯 Recommendation

Evaluate market segment performance beyond reservation volume and revenue by analyzing:

ADR (Average Daily Rate) by Market Segment
RevPAR Contribution
Occupancy Contribution
Average Length of Stay (LOS)
Cancellation Rate
Lead Time
Customer Lifetime Value
Acquisition Cost by Segment
Net Revenue Contribution
Profitability by Market Segment

The objective is to determine which market segments generate the highest long-term value and profitability rather than focusing solely on reservation volume

### 💼 Business Impact

Understanding market segment contribution enables commercial leaders to:

- Optimize sales and marketing investments across customer segments.
- Develop targeted campaigns for high-value traveler groups.
- Improve revenue management and pricing strategies.
- Identify the most valuable sources of demand.
- Increase revenue from profitable market segments.
- Support budgeting and demand forecasting decisions.
- Create a more balanced and resilient demand mix.
- Improve overall portfolio revenue and profitability.

By aligning commercial strategies with the highest-performing market segments, the organization can focus resources on the most valuable customer groups, maximize revenue opportunities, and build a stronger long-term business mix.

| Market Segment | Reservations | Room Revenue | Revenue Share |
| -------------- | -----------: | -----------: | ------------: |
| Leisure        |      253,444 |     $193.17M |        50.64% |
| Corporate      |       94,710 |      $72.36M |        18.97% |
| Direct         |       84,108 |      $63.96M |        16.77% |
| OTA            |       45,340 |      $34.61M |         9.08% |
| Group          |       22,398 |      $17.33M |         4.54% |
