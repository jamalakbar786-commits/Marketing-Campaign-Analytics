
# 📊 Marketing Campaign Analysis Dashboard

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?logo=mysql)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-blueviolet?logo=plotly)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?logo=pandas)
![Status](https://img.shields.io/badge/Project-Completed-success)

### End-to-End Marketing Analytics | Customer Segmentation | KPI Dashboard | Business Intelligence

</div>

---

# 🚀 Project Overview

This project delivers a complete Marketing Campaign Analytics solution that combines:

- Data Cleaning & Feature Engineering
- Exploratory Data Analysis (EDA)
- Customer Segmentation
- SQL-Based KPI Reporting
- Interactive Streamlit Dashboard
- Business Recommendations

The objective is to help business stakeholders understand customer behavior, campaign performance, purchasing trends, and high-value customer segments.

---

# 🎯 Business Problem

A retail company has executed multiple marketing campaigns and collected customer demographic, spending, and campaign response data.

Management requires an analytics solution to:

✅ Identify valuable customers

✅ Measure campaign effectiveness

✅ Understand spending behavior

✅ Analyze purchasing channels

✅ Discover high-response customer segments

✅ Support data-driven marketing decisions

---

# 🏗️ Solution Architecture

```text
Marketing Campaign Dataset
            │
            ▼
 ┌─────────────────────┐
 │ Data Cleaning (EDA) │
 └─────────────────────┘
            │
            ▼
 ┌─────────────────────┐
 │ Feature Engineering │
 └─────────────────────┘
            │
            ▼
 ┌─────────────────────┐
 │      MySQL DB       │
 └─────────────────────┘
            │
            ▼
 ┌─────────────────────┐
 │   SQL KPI Queries   │
 └─────────────────────┘
            │
            ▼
 ┌─────────────────────┐
 │ Streamlit Dashboard │
 └─────────────────────┘
            │
            ▼
 Business Insights & Recommendations
```

---

# 📂 Project Structure

```text
Marketing-Campaign-Analysis/
│
├── app.py
├── config.py
├── dashboard_queries.py
├── load_data.py
├── Marketing_Campaign_Analysis - EDA.ipynb
│
├── screenshots/
│   ├── KPI.png
│   ├── Customer Purchases and Spendings.png
│   ├── Age vs Income Distribution.png
│   ├── Education vs Income Distribution.png
│   ├── Marital Status vs Income Distribution.png
│   └── Family Customer vs Income Distribution.png
│
├── README.md
└── requirements.txt
```

---

# 📊 Dashboard Features

## 1️⃣ KPI Summary Dashboard

Tracks:

- Total Customers
- Average Recency
- Campaign Acceptance Rate
- Average Spend Per Customer
- Average Purchases Per Customer
- Campaign Acceptance Counts
- Response Count
- Complaint Count

### Business Value

Provides a real-time executive summary of campaign performance.

---

## 2️⃣ Customer Spending Analysis

Analyzes spending across:

- Wines
- Fruits
- Meat Products
- Fish Products
- Sweet Products
- Gold Products

### Business Value

Identifies top revenue-generating product categories.

---

## 3️⃣ Purchase Channel Analysis

Analyzes:

- Store Purchases
- Web Purchases
- Catalog Purchases
- Deal Purchases

### Business Value

Determines customer channel preferences.

---

## 4️⃣ Age vs Income Distribution

Helps identify:

- High-value age segments
- Income concentration by age group

---

## 5️⃣ Education vs Income Distribution

Shows income distribution across:

- Basic
- 2n Cycle
- Graduation
- Master
- PhD

---

## 6️⃣ Marital Status vs Income Distribution

Compares:

- Married
- Single
- Together
- Divorced
- Widow

---

## 7️⃣ Family Customer Analysis

Segments:

- Family Customers
- Non-Family Customers

---

# 📸 Dashboard Screenshots

## KPI Dashboard

> Add Screenshot: `1. KPI.png`

---

## Customer Spending & Purchase Analysis

> Add Screenshot: `2. Customer Purchases and Spendings.png`

---

## Age vs Income Distribution

> Add Screenshot: `3. Age vs Income Distribution.png`

---

## Education vs Income Distribution

> Add Screenshot: `4. Education vs Income Distribution.png`

---

## Marital Status vs Income Distribution

> Add Screenshot: `5. Marital Status vs Income Distribution.png`

---

## Family Customer Analysis

> Add Screenshot: `6. Family Customer vs Income Distribution.png`

---

# 📈 Key KPIs

| KPI | Description |
|------|------------|
| Total Customers | Customer Base Size |
| Average Recency | Customer Activity Freshness |
| Campaign Acceptance Rate | Campaign Effectiveness |
| Average Spend | Customer Value |
| Average Purchases | Purchase Frequency |
| Response Count | Positive Campaign Responses |
| Complaint Count | Customer Satisfaction Indicator |

---

# 🔍 Customer Segmentation

The project uses business-driven segmentation rules:

| Segment | Criteria |
|----------|-----------|
| High Income | Income > 75K |
| Young Customer | Age < 30 |
| Campaign Responder | Response = 1 |
| High Web Engagement | Web Visits > 5 |
| Family Customer | Children > 0 |
| High Spender | Top Spending Customers |

---

# 💡 Key Business Insights

### Spending Behavior

- Meat Products and Wines generate the highest revenue.
- Fruits and Sweet Products contribute the least spending.

### Purchase Behavior

- Store purchases dominate customer transactions.
- Web purchases are the second-most preferred channel.

### Demographic Insights

- Middle-income customers represent the majority of the customer base.
- Graduates form the largest customer segment.

### Household Insights

- Family customers dominate low-to-mid income brackets.
- Higher-income groups contain a larger share of non-family customers.

---

# 🎯 Business Recommendations

## Recommendation 1

Focus marketing budget on:

- Meat Products
- Wines

These categories contribute the largest spending share.

---

## Recommendation 2

Increase Digital Marketing Investment

- Email Campaigns
- Website Promotions
- Personalized Recommendations

---

## Recommendation 3

Target Mid-to-High Income Customers

Customers within:

- 50K–75K
- 75K–100K

represent strong purchasing potential.

---

## Recommendation 4

Retarget Campaign Responders

Build loyalty programs around customers with previous positive responses.

---

## Recommendation 5

Develop Family-Oriented Promotions

Create bundled offers and seasonal campaigns targeting family households.

---

## Recommendation 6

Improve Retention Strategy

Use recency metrics to identify inactive customers and launch re-engagement campaigns.

---

# 🛠️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/marketing-campaign-analysis.git
cd marketing-campaign-analysis
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Database

Update:

```python
config.py
```

with your MySQL credentials.

## Run Streamlit Dashboard

```bash
streamlit run app.py
```

---

# 📚 Skills Demonstrated

### Python

- Data Cleaning
- Feature Engineering
- EDA

### SQL

- Aggregations
- KPI Computation
- Customer Segmentation
- Analytical Reporting

### Visualization

- Plotly
- Streamlit
- Interactive Dashboard Design

### Business Analytics

- Customer Analytics
- Marketing Analytics
- Segmentation
- Campaign Performance Analysis

---

# 🌟 Future Enhancements

- Machine Learning Campaign Prediction
- Customer Lifetime Value Modeling
- RFM Segmentation
- Marketing Attribution Analysis
- Automated Reporting

---

# 👨‍💻 Author

### Jamal Akbar

Marketing Analytics | Data Analytics | SQL | Python | Streamlit

If you found this project useful, consider giving it a ⭐ on GitHub.
