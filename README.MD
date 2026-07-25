# Hotel Performance Optimizer V2

## Business Objectives

The objective of HPO V2 is to enable hotel leadership and commercial teams to:

- Monitor commercial performance
- Identify revenue opportunities
- Understand performance drivers
- Forecast future demand and revenue
- Optimize pricing and channel strategy
- Support data-driven decision making
- Measure the business impact of actions taken

## Framework

1. Descriptive Analytics
   → What happened?

2. Diagnostic Analytics
   → Why did it happen?

3. Predictive Analytics
   → What will happen?

4. Prescriptive Analytics
   → What should we do?

5. Impact Measurement & Feedback Loop
   → Did it work?

## Business Value

HPO V2 transforms hospitality data into actionable commercial insights by enabling leadership teams to:

- Improve revenue performance
- Increase forecast accuracy
- Optimize channel and segment strategy
- Reduce cancellation risk
- Support proactive decision-making

The platform is designed to move beyond reporting and support strategic commercial decisions across the EMEA region.

## Technology Stack

Data Warehouse

- Snowflake

Data Transformation

- dbt

Analysis

- SQL
- Python

Data Visualization

- Power BI

Version Control

- GitHub

Analytics Domains

- Descriptive Analytics
- Diagnostic Analytics
- Predictive Analytics
- Prescriptive Analytics

## Analytics Deliverables

### SQL Layer

- KPI Calculations
- Business Question Analysis
- Trend Analysis
- Validation Queries

### Python Layer

- Exploratory Data Analysis (EDA)
- Correlation Analysis
- Root Cause Analysis
- Forecasting Models
- Scenario Analysis

### Power BI Layer

- Executive Dashboard
- Revenue Dashboard
- Segment Dashboard
- Channel Dashboard
- Forecast Dashboard
- Recommendations Dashboard

## Stakeholder Questions

General Manager

- How is my hotel performing?

Revenue Manager

- How can I optimize ADR and RevPAR?

Commercial Director

- Which segments and channels drive revenue?

VP Commercial

- Where are the largest growth opportunities?

## Key Stakeholders

- General Managers
- Revenue Managers
- Commercial Directors
- VP Commercial Services
- EMEA Analytics Team
- Regional Leadership

## Success Metrics

Business Success

- Increase RevPAR
- Increase Direct Booking Share
- Reduce Cancellation Rate
- Improve Forecast Accuracy
- Improve Revenue Growth

Analytics Success

- Dashboard Adoption
- Data Accuracy
- Report Performance
- Forecast Accuracy
- Recommendation Effectiveness

## "EMEA Commercial Performance & Revenue Optimization Dashboard" POWER BI

with these 6 modules:

Executive Summary
Revenue Performance
Segment Analysis
Channel Analysis
Cancellation Analysis
Revenue Opportunities & Recommendations

## TOP KPI's

- Revenue
- Revenue Growth %
- ADR
- Occupancy %
- RevPAR
- Booking Pace
- Booking Lead Time
- Average Length of Stay (ALOS)
- Market Segment Performance
- Channel Performance
- Cancellation Rate
- Direct Booking Share

## Executive KPI Scorecard

- Total Revenue
- Revenue Growth %
- ADR
- Occupancy %
- RevPAR
- Total Bookings
- Booking Pace
- Average Lead Time
- Average Length of Stay (ALOS)
- Cancellation Rate
- Direct Booking Share
- OTA Share
- Forecast Accuracy

## KPI Definitions

### Revenue KPIs

#### Total Revenue

Total Revenue =
SUM(Room Revenue)

Measures the total revenue generated from room bookings.

---

#### Room Revenue

Room Revenue =
SUM(Room Revenue)

Revenue generated from the sale of guestrooms.

---

#### Revenue Growth %

Revenue Growth % =
((Current Period Revenue - Previous Period Revenue) / Previous Period Revenue) × 100

Measures revenue growth between periods.

---

### Occupancy & Rate KPIs

#### Occupancy %

Occupancy % =
Rooms Sold / Rooms Available × 100

Measures the percentage of available rooms sold.

---

#### ADR (Average Daily Rate)

ADR =
Room Revenue / Rooms Sold

Measures the average revenue earned per occupied room.

---

#### RevPAR (Revenue Per Available Room)

RevPAR =
Room Revenue / Rooms Available

Measures revenue generated from all available rooms.

Alternative Formula:

RevPAR =
ADR × Occupancy %

---

### Reservation & Demand KPIs

#### Total Bookings

Total Bookings =
COUNT(Reservations)

Measures total reservation volume.

---

#### Booking Pace

Booking Pace =
Current Period Bookings / Bookings at Same Point Last Year × 100

Measures the speed at which reservations are being accumulated compared to a reference period.

---

#### Booking Lead Time

Booking Lead Time =
Arrival Date - Booking Date

Measures how far in advance guests make reservations.

---

#### Average Lead Time

Average Lead Time =
AVG(Arrival Date - Booking Date)

Measures average advance booking behavior.

---

#### Average Length of Stay (ALOS)

ALOS =
Total Room Nights / Total Reservations

Measures the average number of nights guests stay.

Alternative Formula:

ALOS =
AVG(Length of Stay)

---

#### Room Nights

Room Nights =
SUM(Nights Stayed)

Measures the total number of occupied room nights.

---

### Cancellation KPIs

#### Cancellation Rate

Cancellation Rate =
Cancelled Reservations / Total Reservations × 100

Measures the percentage of reservations canceled.

---

#### Cancelled Revenue

Cancelled Revenue =
SUM(Room Revenue of Cancelled Reservations)

Measures potential revenue lost due to cancellations.

---

### Market Segment KPIs

#### Segment Revenue

Segment Revenue =
SUM(Room Revenue) by Market Segment

Measures revenue contribution by customer segment.

---

#### Segment Contribution %

Segment Contribution % =
Segment Revenue / Total Revenue × 100

Measures each segment's contribution to total revenue.

---

### Channel Performance KPIs

#### Channel Revenue

Channel Revenue =
SUM(Room Revenue) by Booking Channel

Measures revenue generated from each booking channel.

---

#### Channel Contribution %

Channel Contribution % =
Channel Revenue / Total Revenue × 100

Measures channel contribution to total revenue.

---

#### Direct Booking Share

Direct Booking Share =
Direct Booking Revenue / Total Revenue × 100

Measures the percentage of revenue generated from direct channels.

---

#### OTA Share

OTA Share =
OTA Revenue / Total Revenue × 100

Measures dependency on Online Travel Agencies.

---

### Customer KPIs

#### Repeat Guest %

Repeat Guest % =
Repeat Guests / Total Guests × 100

Measures customer loyalty and retention.

---

#### Unique Guests

Unique Guests =
COUNT(DISTINCT Guest ID)

Measures the number of individual guests.

---

### Forecasting KPIs

#### Forecast Occupancy

Forecast Occupancy =
Predicted Rooms Sold / Available Rooms × 100

Measures expected future occupancy.

---

#### Forecast ADR

Forecast ADR =
Predicted Room Revenue / Predicted Rooms Sold

Measures expected room rate performance.

---

#### Forecast RevPAR

Forecast RevPAR =
Predicted Room Revenue / Available Rooms

Measures expected future revenue performance.

---

#### Forecast Accuracy

Forecast Accuracy =
(1 - ABS(Actual - Forecast) / Actual) × 100

Measures forecast model performance.

---

---

#### Forecast Error %

Forecast Error % =
ABS(Actual - Forecast) / Actual × 100

Measures forecasting error and model reliability.

---

### Commercial Performance KPIs

#### Revenue per Booking

Revenue per Booking =
Total Revenue / Total Bookings

Measures average revenue generated per reservation.

---

#### Revenue per Guest

Revenue per Guest =
Total Revenue / Total Guests

Measures guest value contribution.

---

#### Revenue per Room Type

Revenue per Room Type =
SUM(Room Revenue) by Room Type

Measures revenue contribution by room category.

---

#### Revenue Concentration %

Revenue Concentration % =
Top Revenue Hotels / Total Revenue × 100

Measures how much revenue is concentrated among top-performing properties.

## Revenue Metrics

Occupancy %
ADR
RevPAR
Revenue Growth %
Room Revenue
Total Revenue

## Commercial Metrics

Booking Pace
Lead Time
Cancellation Rate
Market Segment Performance
Channel Performance
Direct vs OTA Contribution

---

### Hotel Performance KPIs

#### Revenue per Hotel

Revenue per Hotel =
SUM(Room Revenue) by Hotel

Measures revenue contribution by property.

---

#### Hotel Contribution %

Hotel Revenue / Total Revenue × 100

Measures each hotel's contribution to total revenue.

---

#### Revenue Rank

RANK() based on Hotel Revenue

Measures relative hotel performance.

---

## Solution Architecture

Source Systems
↓
Snowflake Data Warehouse
↓
dbt Transformation Layer
↓
Analytics Models
↓
SQL Analysis
↓
Python EDA & Forecasting
↓
Power BI
↓
Executive Decision Making

## HPOv2 Workflow

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
Validate Results
↓
EDA
↓
Validate Results
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

## Business Questions Workflow

Snowflake SQL
↓
Answer Business Questions
↓
Generate KPI Findings
↓
Python EDA
↓
Identify Drivers & Root Causes
↓
Diagnostic Insights
↓
Predictive Models
↓
Prescriptive Recommendations
↓
Power BI Dashboard
↓
Executive Storytelling

## Executive Storytelling Framework

Observation
↓
Insight
↓
Recommendation
↓
Business Impact

Example:

Observation:
OTA cancellation rate = 22%

Insight:
OTA bookings contribute 60% of total cancellations

Recommendation:
Implement stricter OTA cancellation policies

Expected Impact:
Recover approximately $800K in annual room revenue

## Data Quality Framework

Validation Layer 1

- Record Counts

Validation Layer 2

- Primary Key Uniqueness

Validation Layer 3

- Duplicate Detection

Validation Layer 4

- Revenue Reconciliation

Validation Layer 5

- KPI Validation

Validation Layer 6

- Business Sign-off

## ## Case Studies

- How do you identify revenue opportunities
- What would you do if RevPAR declines by 10%?
- Hotel occupancy dropped from 82% to 74% this quarter. How would you investigate?"
- Occupancy dropped from 80% to 70%.
- Revenue increased but RevPAR declined.
- OTA bookings increased significantly.
- A hotel GM says the dashboard numbers are wrong.

## CASE STUDY #2

Market Segment Optimization
Business Scenario
A Commercial Director asks:

Which market segments are driving profitability?

Questions
Revenue by Segment

Leisure
Corporate
Group
Wholesale
Government

Analyze:

Revenue
ADR
Occupancy
RevPAR
Length of Stay

Executive Questions
Highest Revenue Segment?
Highest ADR Segment?
Highest RevPAR Segment?
Lowest Performing Segment?
Which Segment Has Growth Potential?
Recommendations
Example:

Corporate generates the highest ADR but lower volume. Sales teams should target corporate account acquisition.

## CASE STUDY #3

Booking Channel Analysis
Business Problem
Management wants to reduce OTA dependency.
Questions
Revenue by Channel:

Direct
OTA
GDS
Voice
Property Direct

Analyze:

Revenue
ADR
Room Nights
Booking Volume

Executive Questions
Which Channel Produces Most Revenue?
Which Channel Produces Highest ADR?
Which Channel Has Lowest Cancellation Rate?
How Dependent Are We On OTA?
Recommendation
Example:

45% of bookings originate from OTA channels. Increasing direct booking share by 10% could improve profitability by reducing commission expenses.

## CASE STUDY #4

Cancellation Analysis
Business Problem
Several hotels report revenue leakage due to cancellations.
Questions
Analyze:

Cancellation Rate
Cancelled Revenue
Segment Cancellation Rate
Channel Cancellation Rate

Executive Questions
Which Segment Cancels Most?
Which Channel Has Highest Cancellations?
Which Hotels Have Highest Cancellation Rates?
How Much Revenue Is Lost Due To Cancellations?
Recommendation
Example:

Leisure OTA bookings have a 22% cancellation rate. Introduce non-refundable promotional rates during peak periods.

CASE STUDY #5
Lead Time Analysis
Business Problem
Revenue Management wants to optimize forecasting.
Questions
Analyze:

Average Lead Time
Revenue by Lead Time Bucket

Buckets:

0-7 days
8-30 days
31-60 days
61-90 days
90+ days

Executive Questions
When Do Guests Typically Book?
Which Lead Time Generates Most Revenue?
Which Segment Books Furthest In Advance?
Recommendation
Example:

Group demand books 90+ days ahead. Marketing campaigns should be launched earlier to capture long-lead demand.

## CASE STUDY #6

Geographic Performance Analysis
Business Problem
EMEA Leadership wants to understand market performance.
Questions
Analyze:

Revenue by Country
Revenue by City
ADR by Country
Occupancy by Country

Executive Questions
Highest Revenue Country?
Highest RevPAR Country?
Fastest Growing Country?
Underperforming Markets?
Recommendation
Example:

UAE contributes 35% of revenue but growth is slowing. Saudi Arabia shows stronger year-over-year growth and should receive additional commercial focus.

## CASE STUDY #7

Executive Dashboard (Interview-Winning Project)
This is the case study I would present if I were you.
Scenario
You are the Analytics Manager for EMEA.
The VP asks:

"Give me a 5-minute overview of the business and tell me where I should focus."

Dashboard Sections
Executive KPIs

Total Revenue
Occupancy %
ADR
RevPAR
Room Nights
Cancellation Rate

Trends

Revenue Trend
ADR Trend
Occupancy Trend

Hotel Rankings

Top Hotels
Bottom Hotels

Segment Analysis

Best Segment
Worst Segment

Channel Analysis

Direct vs OTA

Opportunity Analysis
Visual:
Top 5 Revenue Opportunities
Example:

OpportunityImpactIncrease Direct BookingsHighReduce OTA DependenceHighImprove Corporate SegmentMediumReduce CancellationsHighImprove Low Performing HotelsMedium

Expected approach:

Step 1
Define the problem.

Step 2
Break down KPIs:

Occupancy
ADR
RevPAR
Revenue

Step 3
Segment analysis:

Property
Country
Brand
Market Segment
Booking Channel

Step 4
Identify drivers.

Step 5
Recommend actions.

## Case Study #8

EMEA Regional Performance Review

Business Scenario:

The VP Commercial Services requests a quarterly review
of EMEA hotel performance.

Questions:

- Which countries exceeded targets?
- Which countries missed targets?
- What drove performance differences?
- Which regions require intervention?
- What actions should leadership prioritize?

Deliverables:

- Executive Summary
- Country Rankings
- Revenue Drivers
- Risk Assessment
- Top 5 Opportunities
- Leadership Recommendations

## Validation Questions

- How do you validate a KPI?

- How do you know your dashboard numbers are correct?

- What checks would you perform after a join?

## Strong answer

- Validate grain

- Check duplicates

- Verify primary keys

- Check record counts

- Reconcile totals with source systems

- Obtain business sign-off

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
- What was the average number of bookings per customer?

---

## 2. Diagnostic Analytics

### Why did it happen? (Root Cause Analysis)

### Revenue Performance (Diagnostic)

- Why did RevPAR increase or decrease?
- Was revenue performance driven by ADR or Occupancy?
- Which properties contributed most to revenue changes?
- Which hotels contributed most to Revenue Growth %?
- Which hotels experienced the largest revenue declines?
- Did revenue growth occur across the portfolio or only in a few properties?
- What percentage of total revenue comes from the top-performing hotels?
- Which market segments impacted revenue performance?
- Which customer segments generated the greatest incremental revenue?
- Which booking channels contributed most to revenue growth?
- Did channel mix changes influence overall revenue performance?
- Did luxury room categories drive revenue growth?
- Did specific room types contribute disproportionately to revenue?
- Which months contributed the most to annual revenue performance?
- Were revenue declines concentrated in specific hotels?
- Did changes in reservation volume influence revenue trends?
- Did changes in booking pace impact revenue performance?
- Did changes in average length of stay impact revenue performance?
- Did cancellation trends negatively affect revenue growth?
- Did customer repeat business contribute to revenue growth?
- Was revenue growth supported by higher pricing or higher demand?
- Were revenue gains driven by higher booking volume or higher room rates?
- Which geographic markets contributed most to revenue growth?
- Which combinations of hotel, market segment, and channel generated the highest revenue?

### RevPAR Analysis

- Was RevPAR growth driven by ADR or Occupancy?
- Which hotels experienced the strongest RevPAR growth?
- Which room categories generated the highest RevPAR?
- Which periods experienced significant RevPAR fluctuations?
- Did RevPAR performance differ across market segments?
- Which booking channels contributed to RevPAR improvement?
- Did cancellations negatively impact RevPAR performance?
- Which hotels experienced declining RevPAR despite revenue growth?
- Which revenue drivers had the strongest correlation with RevPAR growth?

### ADR Analysis

- Why did ADR increase or decrease?
- Which room types achieved the highest ADR?
- Which channels generated the highest ADR?
- Which market segments paid the highest ADR?
- Which hotels achieved the highest ADR growth?
- Did ADR changes vary significantly by hotel?
- Were ADR improvements concentrated in premium room categories?
- Did occupancy pressure lead to ADR reductions?
- Did pricing strategy changes influence ADR performance?
- During which periods was ADR highest?
- Which customer segments were willing to pay premium rates?

### Occupancy Analysis

- Why was occupancy below forecast?
- Which time periods experienced occupancy declines?
- Did cancellation activity impact hotel demand?
- Did booking lead times shift compared to previous periods?
- Which hotels experienced the largest occupancy declines?
- Were occupancy changes driven by specific market segments?
- Did certain room types remain unsold more frequently?
- Which periods achieved peak occupancy?
- Did occupancy vary significantly by hotel category?
- Was occupancy impacted by shorter booking windows?
- Did repeat customers help maintain occupancy levels?
- Were occupancy declines linked to lower reservation volumes?
- Which properties consistently achieved above-average occupancy?

### Booking Analysis

- Why did booking volume increase or decrease?
- Which hotels generated the most reservations?
- Which channels drove booking growth?
- Which customer segments showed declining bookings?
- Were booking trends consistent across all properties?
- Did lead times change booking behavior?
- Were bookings concentrated in specific seasons?
- Which room categories experienced the largest booking growth?
- Did customer retention influence booking volume?
- Did higher cancellations offset booking growth?
- Which periods experienced the strongest booking pickup?
- Which booking drivers had the greatest impact on demand?

### Cancellation Analysis

- Why did cancellation rates increase?
- Which channels generated the highest cancellation rates?
- Which market segments produced the most cancellations?
- Did longer lead times result in higher cancellations?
- Which hotels experienced abnormal cancellation levels?
- Were cancellations concentrated during specific seasons?
- Which room types had the highest cancellation rates?
- Did cancellation volume materially impact occupancy?
- Did cancellations significantly affect revenue performance?
- Were repeat guests less likely to cancel?
- Which customer segments had the lowest cancellation risk?

### Channel Analysis

- Which booking channels contributed to revenue growth?
- Which channels produced the highest ADR?
- Which channels produced the highest cancellation rates?
- Which channels generated the most profitable bookings?
- Which channels delivered the highest RevPAR?
- Which channels produced the longest stays?
- Which channels generated the shortest booking lead times?
- Which channels attracted repeat customers?
- Which channels generated the highest occupancy contribution?
- Which channels showed declining performance over time?
- Which channel had the strongest balance of revenue, occupancy, and ADR?
- Did channel mix changes influence commercial performance?

### Market & Segment Analysis

- Why did one hotel outperform another?
- Which customer segments drove growth?
- Which customer segments showed declining demand?
- Which room categories had the highest contribution to revenue?
- Which segments generated the highest ADR?
- Which segments generated the highest occupancy?
- Which segments delivered the longest stays?
- Which segments produced the most repeat customers?
- Which segments generated the lowest cancellation rates?
- Which segments drove RevPAR growth?
- Which segments were most sensitive to pricing changes?
- Which segments contributed most to booking growth?
- Which segments generated the greatest revenue per booking?
- Which segments provided the best balance of volume and profitability?

### Guest Behavior Analysis

- Did guest booking behavior change over time?
- Did booking lead times increase or decrease?
- Which customers booked furthest in advance?
- Which customers stayed the longest?
- Were repeat customers more valuable than first-time guests?
- Did repeat guests generate higher revenue?
- Which guests were most likely to cancel?
- Did customer loyalty correlate with longer stays?
- Did short lead-time bookings generate lower ADR?
- Which customer groups generated the highest lifetime value?
- How did guest behavior differ across segments and channels?

### Room Type Performance Analysis

- Which room types generated the highest revenue?
- Which room types generated the highest ADR?
- Which room types achieved the highest occupancy?
- Which room types experienced declining demand?
- Did premium rooms contribute disproportionately to revenue?
- Which room types had the highest cancellation rates?
- Which room categories produced the longest stays?
- Which room types delivered the strongest RevPAR?
- Did room mix changes impact overall hotel revenue?
- Which room types remained underutilized?
- Which room types generated the highest revenue per booking?

---

## 3. Predictive Analytics

### What will happen? (Forecasting & Modeling)

### Demand Forecasting

- What will occupancy be over the next 30, 60, and 90 days?
- What future periods are expected to experience high demand?
- Which future periods are expected to experience low demand?
- Which hotels are expected to exceed occupancy targets?
- Which hotels are expected to underperform?
- Which properties are at risk of occupancy declines?
- Which markets are expected to experience the strongest demand growth?
- Which market segments are expected to drive future demand?
- Which room types are expected to experience the highest demand?
- When are future occupancy peaks expected to occur?
- When are future occupancy troughs expected to occur?
- What is the expected booking pace for upcoming periods?

### Revenue Forecasting

- What will room revenue be over the forecast horizon?
- What will ADR be over the forecast horizon?
- What will RevPAR be over the forecast horizon?
- Which hotels are expected to generate the highest future revenue?
- Which hotels are at risk of missing revenue targets?
- Which market segments are expected to generate the most revenue?
- Which booking channels are expected to generate the most revenue?
- What revenue opportunities are expected in future periods?
- What revenue risks are expected in future periods?
- Which countries or markets are expected to drive revenue growth?
- What is the projected Revenue Growth % over the forecast horizon?
- How will changes in ADR impact future revenue performance?

### Booking Forecasting

- How many bookings are expected before arrival dates?
- What booking pickup is expected over time?
- How will booking lead times impact future demand?
- What booking volume is expected by hotel?
- What booking volume is expected by market segment?
- What booking volume is expected by channel?
- Which future periods are expected to experience booking surges?
- Which future periods may require demand stimulation?
- How will seasonality impact future booking trends?
- What percentage of future bookings is expected from repeat guests?

### Cancellation Prediction

- Which reservations are likely to cancel?
- What future cancellation rate is expected?
- What revenue risk exists due to future cancellations?
- Which channels are expected to generate the most cancellations?
- Which market segments are expected to have the highest cancellation rates?
- Which properties are most exposed to cancellation risk?
- What amount of forecasted revenue is at risk due to cancellations?
- Which bookings have the highest probability of cancellation?
- How will cancellations impact future occupancy forecasts?
- How will cancellations impact future RevPAR forecasts?

### Customer & Loyalty Forecasting

- What percentage of guests are expected to be repeat customers?
- Which customer segments are expected to show the highest growth?
- Which customer groups are expected to generate the highest lifetime value?
- How will repeat guest behavior impact future revenue?
- Which customer segments are at risk of declining demand?

### Scenario Forecasting

- What happens if ADR increases by 5%?
- What happens if occupancy declines by 10%?
- What is the expected impact of reducing cancellation rates?
- What is the expected impact of increasing direct booking share?
- What is the expected impact of improving booking pace?
- What revenue uplift could be achieved under different demand scenarios?
- What is the best-case, expected, and worst-case revenue forecast?

---

## 4. Prescriptive Analytics

### How can we make it happen? (Optimization & Decision Support)

### Pricing Optimization

- Should ADR be increased or decreased?
- What ADR maximizes expected revenue?
- What pricing actions should be taken to improve RevPAR?
- Which hotels should adjust pricing immediately?
- Which room types should receive rate increases?
- Which room types require price reductions to stimulate demand?
- What pricing strategy maximizes both occupancy and revenue?
- Which periods can support premium pricing?
- Which periods require promotional pricing?
- What is the projected revenue impact of pricing changes?

### Demand Optimization

- Which periods require promotional campaigns?
- Which hotels need demand stimulation?
- Which room types should receive pricing adjustments?
- Which hotels require immediate occupancy improvement actions?
- Which future low-demand periods should be targeted with campaigns?
- Which market segments should be targeted to increase demand?
- Which customer segments offer the greatest growth opportunity?
- How can occupancy be increased without significantly reducing ADR?
- Which properties should receive additional marketing support?
- What actions will generate the highest occupancy improvement?

### Channel Optimization

- Which channels should receive additional investment?
- Which channels should be deprioritized?
- How can channel mix be optimized to maximize profitability?
- How can direct booking share be increased?
- Which channels produce the highest net revenue?
- Which channels should receive additional inventory allocation?
- Which channels have excessive cancellation rates?
- Which channels generate the best balance of ADR and occupancy?
- Which channels should be targeted for customer acquisition?
- What is the projected impact of improving direct booking share?

### Market Segment Optimization

- Which market segments should receive increased sales focus?
- Which market segments should be targeted during low-demand periods?
- Which segments generate the highest revenue contribution?
- Which segments produce the highest ADR?
- Which segments generate the strongest RevPAR performance?
- Which segments should receive promotional offers?
- Which segments are underperforming but have growth potential?
- How should demand be balanced across customer segments?
- Which segments provide the best balance of volume and profitability?
- What commercial actions will maximize segment growth?

### Inventory & Room Type Optimization

- Which room types should be protected for high-value demand?
- Which room types should receive promotional offers?
- Which room categories should receive inventory restrictions?
- Which room types are underutilized?
- Which room types generate the strongest revenue contribution?
- Which room categories should be prioritized during high-demand periods?
- Which room types should be bundled with value-added offers?
- How can room inventory allocation maximize revenue?
- What room mix generates the highest RevPAR?
- Which room types represent the greatest revenue opportunity?

### Cancellation Risk Mitigation

- Which bookings require proactive cancellation prevention actions?
- Which channels should have stricter cancellation policies?
- Which market segments generate excessive cancellation risk?
- Which hotels require cancellation reduction initiatives?
- How much revenue can be recovered through cancellation reduction?
- Should deposits or non-refundable rates be introduced?
- Which bookings should be targeted with retention campaigns?
- What actions will most effectively reduce cancellation rates?
- What is the forecasted revenue recovery from reducing cancellations?

### Revenue Optimization

- What actions will maximize room revenue?
- What commercial strategies are expected to produce the highest revenue lift?
- What is the estimated business impact of each recommendation?
- Which opportunities provide the highest revenue upside?
- Which hotels require immediate revenue intervention?
- What combination of pricing, channels, and segments maximizes revenue?
- Which actions will have the greatest impact on RevPAR?
- Which actions will improve both ADR and occupancy?
- What is the expected ROI of each recommendation?
- Which revenue opportunities should be prioritized first?

### Automated Recommendations

- What actions should hotel leadership take today?
- Which performance risks require immediate attention?
- Which opportunities provide the highest expected return?
- What is the estimated revenue uplift from each recommended action?
- What are the top 5 recommended actions by projected business impact?
- Which recommendations should be implemented immediately?
- Which recommendations should be monitored over time?
- Which hotels require executive intervention?
- What is the expected revenue uplift from the recommendation portfolio?
- Which actions have the highest confidence score?

### Scenario Planning & What-If Analysis

- What happens if ADR increases by 5%?
- What happens if occupancy decreases by 5%?
- What happens if direct booking share increases by 10%?
- What happens if cancellation rates decrease by 5%?
- What happens if booking pace accelerates?
- What is the revenue impact of shifting demand to direct channels?
- What is the revenue impact of improving segment mix?
- What is the best-case revenue scenario?
- What is the worst-case revenue scenario?
- Which scenario generates the highest expected RevPAR?

---

## 5. Impact Measurement & Feedback Loop

### Did the action work?

### Performance Measurement

- Did occupancy improve after the recommended action?
- Did ADR improve after implementation?
- Did RevPAR improve after implementation?
- Did room revenue increase after implementation?
- Did booking pace improve after action was taken?
- Did direct booking share increase?
- Did cancellation rates decrease?
- Did market segment performance improve?
- Did channel performance improve?
- Did underperforming hotels improve performance?
- Were commercial targets achieved?
- Was forecast accuracy acceptable?

### Business Impact

- How much additional revenue was generated?
- How much RevPAR growth was achieved?
- How much ADR improvement was achieved?
- How much occupancy improvement was achieved?
- How much revenue was recovered from reduced cancellations?
- How much revenue was generated from pricing optimization?
- How much revenue was generated from channel optimization?
- Which recommendations produced the greatest impact?
- Which recommendations produced the highest ROI?
- Which actions should be repeated?
- Which actions should be adjusted or discontinued?
- What was the estimated vs actual business impact?

### Recommendation Effectiveness

- Which recommendations were implemented?
- Which recommendations delivered expected results?
- Which recommendations underperformed expectations?
- What percentage of recommendations delivered measurable value?
- Which recommendation category generated the greatest impact?
- How accurate were projected revenue uplift estimates?
- Which recommendations should become standard business practice?

### Forecast & Model Performance

- How accurate were occupancy forecasts?
- How accurate were ADR forecasts?
- How accurate were RevPAR forecasts?
- How accurate were revenue forecasts?
- How accurate were cancellation predictions?
- Which forecasting models performed best?
- Which forecasting models require retraining?
- Did model performance improve over time?
- Were prediction errors within acceptable thresholds?

### Dashboard & Analytics Adoption

- Are stakeholders actively using the dashboard?
- Which dashboard pages are used most frequently?
- Which KPIs are viewed most often?
- Are leadership teams acting on recommendations?
- Is dashboard adoption increasing over time?
- Are business decisions becoming more data-driven?
- Are users satisfied with dashboard performance and insights?

### Continuous Improvement

- How can forecasting models be improved?
- How can recommendation accuracy be increased?
- Which new data sources should be integrated?
- Which KPIs require refinement?
- Which business rules require adjustment?
- What new business questions should be investigated?
- What additional predictive models should be developed?
- What additional optimization opportunities exist?
- How can the analytics workflow be further automated?
- What lessons learned should be incorporated into future analysis?

### Feedback Loop

- Measure Results
- Compare Actual vs Forecast
- Evaluate Recommendation Performance
- Capture Business Feedback
- Improve Models
- Generate Better Recommendations
- Repeat

## Project Outcomes

HPO V2 demonstrates an end-to-end commercial analytics solution that:

- Centralizes hospitality data within Snowflake
- Transforms raw data using dbt
- Answers strategic business questions through SQL
- Identifies performance drivers using Python EDA
- Performs diagnostic and root cause analysis
- Predicts future performance through forecasting models
- Recommends revenue optimization actions
- Measures business impact through a closed feedback loop

The solution enables hotel leadership to move from reactive reporting to proactive decision-making by leveraging descriptive, diagnostic, predictive, and prescriptive analytics.

## End-to-End Analytics Lifecycle

Business Objectives
↓
Data Collection
↓
Data Warehouse (Snowflake)
↓
Data Transformation (dbt)
↓
SQL Analysis
↓
Descriptive Analytics
↓
Diagnostic Analytics
↓
Predictive Analytics
↓
Prescriptive Analytics
↓
Impact Measurement
↓
Executive Decision Making

## HPO V2 Value Proposition

HPO V2 is designed to help hotel leadership teams answer five critical questions:

1. What happened?
   - Descriptive Analytics

2. Why did it happen?
   - Diagnostic Analytics

3. What will happen next?
   - Predictive Analytics

4. What should we do about it?
   - Prescriptive Analytics

5. Did our actions work?
   - Impact Measurement & Feedback Loop

By combining Snowflake, dbt, SQL, Python, and Power BI, HPO V2 delivers a modern hospitality analytics platform aligned with commercial, revenue management, and executive decision-making needs across the EMEA region.
