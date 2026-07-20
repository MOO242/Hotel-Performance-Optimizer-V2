# Business Questions

The Hotel Performance Optimization V2 (HPO V2) Commercial Analytics Framework is designed to answer key commercial, revenue, and performance questions across four analytics domains: Descriptive, Diagnostic, Predictive, and Prescriptive Analytics.

---

## 1. Descriptive Analytics

### What happened? (Historical Reporting)

#### Revenue Performance

- What was the total Room Revenue?
- What was the RevPAR trend over time?
- What was the ADR trend over time?
- What was the Occupancy trend over time?
- Which hotels generated the highest revenue?
- Which hotels underperformed expectations?

#### Booking Performance

- How many bookings were received?
- Which booking channels generated the most reservations?
- Which market segments generated the most revenue?
- Which room types had the highest demand?
- What were the peak booking periods?

#### Guest Behavior

- What was the average Booking Lead Time?
- What was the Average Length of Stay (ALOS)?
- What was the Cancellation Rate?
- What percentage of guests were repeat customers?

---

## 2. Diagnostic Analytics

### Why did it happen? (Root Cause Analysis)

#### Revenue Analysis

- Why did RevPAR increase or decrease?
- Was revenue performance driven by ADR or Occupancy?
- Which properties contributed most to revenue changes?
- Which market segments impacted revenue performance?

#### Occupancy Analysis

- Why was occupancy below forecast?
- Which time periods experienced occupancy declines?
- Did cancellation activity impact hotel demand?
- Did booking lead times shift compared to previous periods?

#### Channel Analysis

- Which booking channels contributed to revenue growth?
- Which channels produced the highest ADR?
- Which channels produced the highest cancellation rates?
- Which channels generated the most profitable bookings?

#### Market & Segment Analysis

- Why did one hotel outperform another?
- Which customer segments drove growth?
- Which customer segments showed declining demand?
- Which room categories had the highest contribution to revenue?

---

## 3. Predictive Analytics

### What will happen? (Forecasting & Modeling)

#### Demand Forecasting

- What will occupancy be over the next 30, 60, and 90 days?
- What future periods are expected to experience high demand?
- Which hotels are expected to exceed occupancy targets?
- Which hotels are expected to underperform?

#### Revenue Forecasting

- What will ADR be over the forecast horizon?
- What will RevPAR be over the forecast horizon?
- What will room revenue be over the forecast horizon?
- What revenue opportunities are expected in future periods?

#### Booking Forecasting

- How many bookings are expected before arrival dates?
- What booking pickup is expected over time?
- How will booking lead times impact future demand?

#### Cancellation Prediction

- Which reservations are likely to cancel?
- What future cancellation rate is expected?
- What revenue risk exists due to future cancellations?

---

## 4. Prescriptive Analytics

### How can we make it happen? (Optimization & Decision Support)

#### Pricing Optimization

- Should ADR be increased or decreased?
- What ADR maximizes expected revenue?
- What pricing actions should be taken to improve RevPAR?

#### Demand Optimization

- Which periods require promotional campaigns?
- Which hotels need demand stimulation?
- Which room types should receive pricing adjustments?

#### Channel Optimization

- Which channels should receive additional investment?
- Which channels should be deprioritized?
- How can channel mix be optimized to maximize profitability?

#### Revenue Optimization

- What actions will maximize room revenue?
- What commercial strategies are expected to produce the highest revenue lift?
- What is the estimated business impact of each recommendation?

#### Automated Recommendations

- What actions should hotel leadership take today?
- Which performance risks require immediate attention?
- Which opportunities provide the highest expected return?
- What is the estimated revenue uplift from each recommended action?

---

## 5. Impact Measurement & Feedback Loop

### Did the action work?

#### Performance Measurement

- Did occupancy improve after the recommended action?
- Did ADR improve after implementation?
- Did RevPAR improve after implementation?
- Was forecast accuracy acceptable?

#### Business Impact

- How much additional revenue was generated?
- Which recommendations produced the greatest impact?
- Which actions should be repeated?
- Which actions should be adjusted or discontinued?

#### Continuous Improvement

- How can forecasting models be improved?
- How can recommendation accuracy be increased?
- What new business questions should be investigated?


Data Sources
    ↓
Snowflake
    ↓
dbt Models
    ↓
Business Questions
    ↓
SQL Analysis
    ↓
EDA
    ↓
Diagnostic Analysis
    ↓
Insights
    ↓
Recommendations
    ↓
Power BI Dashboard
    ↓
Executive Presentation
``


Business Question workflow

↓

SQL Analysis

↓

Result

↓

Business Insight

↓

Recommendation

↓

Business Impact

WORKFLOW: 

Snowflake SQL
     ↓
Answer all business questions
     ↓
Create KPI findings
     ↓
Python EDA WHY?
     ↓
Find drivers and root causes
     ↓
Insights
     ↓
Recommendations
     ↓
Power BI