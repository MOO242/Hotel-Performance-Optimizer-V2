# **1. Descriptive Analytics**

## **What happened? (Historical Reporting)**

---

## **📈 Guest Behavior**

### 13- What was the Average Length of Stay (ALOS)?

```sql
SELECT
    AVG (
        DATEDIFF(
            DAY,
            to_date(
                TO_VARCHAR(check_in_date_key),
                'YYYYMMDD'
            ),
            to_date(
                TO_VARCHAR(checkout_date_key),
                'YYYYMMDD'
            )
        )
    ) AS avg_len_of_stay
FROM
    HPOV2_DB.ANALYTICS.FACT_RESERVATIONS

```

## Business Insight

Average Length of Stay (ALOS) = 2.6 Days

Guests stay an average of 2.62 nights per reservation, indicating predominantly short-stay demand.

## Recommendation

Revenue Management should closely monitor booking pace within the 30-day arrival window and adjust pricing dynamically to capture short-term demand opportunities.

## Business Impact

Increasing ALOS can increase room revenue and occupancy efficiency while reducing operational turnover costs.

---
