import streamlit as st
import pandas as pd
import plotly.express as px

from config import engine
from dashboard_queries import (get_country_kpi_query, get_spend_query, get_purchase_query, 
get_age_vs_income_query, get_education_vs_income_query, get_marital_vs_income_query,
get_family_vs_income_query)                              

st.set_page_config(
    page_title="Marketing Campaign Analytics",
    layout="wide"
)

st.title("Marketing Campaign Summary")

country_filter = st.selectbox(
    "Select Country",
    [
        "All",
        "Spain",
        "Canada",
        "Saudi Arabia",
        "Australia",
        "India",
        "Germany",
        "USA",
        "Mexico"
    ],
    key="kpi_country"
)

query, params = get_country_kpi_query(country_filter)

kpi = pd.read_sql(
    query,
    engine,
    params=params
)

st.subheader(
    f"KPI Summary - {country_filter}"
)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "Total Customers",
        int(kpi["total_customers"][0] or 0)
    )

with col2:
    st.metric(
        "Average Recency",
        round(float(kpi["avg_recency"][0] or 0), 2)
    )

with col3:
    st.metric(
        "Campaign Acceptance Rate (%)",
        f"{float(kpi['campaign_acceptance_rate'][0] or 0):,.2f}%"
    )
    
with col4:
    st.metric(
        "Avg Spend Per Customer",
        f"{float(kpi['avg_spend_per_customer'][0] or 0):,.2f}"
    )

with col5:
    st.metric(
        "Avg Purchases Per Customer",
        f"{float(kpi['avg_purchases_per_customer'][0] or 0):,.2f}"
    )

col6, col7, col8, col9, col10 = st.columns(5)

with col6:
    st.metric(
        "AcceptedCmp1",
        int(kpi["accepted_cmp1"][0] or 0)
    )

with col7:
    st.metric(
        "AcceptedCmp2",
        int(kpi["accepted_cmp2"][0] or 0)
    )

with col8:
    st.metric(
        "AcceptedCmp3",
        int(kpi["accepted_cmp3"][0] or 0)
    )

with col9:
    st.metric(
        "AcceptedCmp4",
        int(kpi["accepted_cmp4"][0] or 0)
    )

with col10:
    st.metric(
        "AcceptedCmp5",
        int(kpi["accepted_cmp5"][0] or 0)
    )

col11, col12, col13, col14, col15 = st.columns(5)

with col11:
    st.metric(
        "Response",
        int(kpi["response_count"][0] or 0)
    )

with col12:
    st.metric(
        "Complain",
        int(kpi["complain_count"][0] or 0)
    )

st.divider()

st.header("Customer Spending & Purchase Analysis")

country_analysis_filter = st.selectbox(
    "Select Country",
    [
        "All",
        "Spain",
        "Canada",
        "Saudi Arabia",
        "Australia",
        "India",
        "Germany",
        "USA",
        "Mexico"
    ],
    key="spend_purchase_country"
)

spend_query, spend_params = get_spend_query(
    country_analysis_filter
)

spend_df = pd.read_sql(
    spend_query,
    engine,
    params=spend_params
)

spend_chart = pd.DataFrame({
    "Category": [
        "Wines",
        "Fruits",
        "Meat Products",
        "Fish Products",
        "Sweet Products",
        "Gold Products"
    ],
    "Amount": [
        spend_df["Wines"][0] or 0,
        spend_df["Fruits"][0] or 0,
        spend_df["MeatProducts"][0] or 0,
        spend_df["FishProducts"][0] or 0,
        spend_df["SweetProducts"][0] or 0,
        spend_df["GoldProducts"][0] or 0
    ]
})

purchase_query, purchase_params = get_purchase_query(
    country_analysis_filter
)

purchase_df = pd.read_sql(
    purchase_query,
    engine,
    params=purchase_params
)

purchase_chart = pd.DataFrame({
    "Category": [
        "Deals",
        "Web",
        "Catalog",
        "Store"
    ],
    "Amount": [
        purchase_df["DealPurchases"][0] or 0,
        purchase_df["WebPurchases"][0] or 0,
        purchase_df["CatalogPurchases"][0] or 0,
        purchase_df["StorePurchases"][0] or 0
    ]
})

col1, col2 = st.columns(2)

with col1:

    spend_fig = px.pie(
        spend_chart,
        names="Category",
        values="Amount",
        hole=0.5,
        title=f"Customer Spending - {country_analysis_filter}"
    )

    spend_fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    st.plotly_chart(
        spend_fig,
        width="stretch"
    )

with col2:

    purchase_fig = px.pie(
        purchase_chart,
        names="Category",
        values="Amount",
        hole=0.5,
        title=f"Customer Purchases - {country_analysis_filter}"
    )

    purchase_fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    st.plotly_chart(
        purchase_fig,
        width="stretch"
    )

st.divider()

# --- ROW 7: Age vs Income Cross-Analysis (Grouped Column Chart) ---

st.subheader("Age vs Income Distribution")

# 1. Fetch cross-tabulated dataset
age_inc_query, age_inc_params = get_age_vs_income_query()
age_inc_df = pd.read_sql(
    age_inc_query,
    engine,
    params=age_inc_params
)

# 2. Add a dynamic filter to isolate this multi-dimensional metric
selected_view = st.selectbox(
    "Select Country",
    options=list(age_inc_df["Country"].unique()),
    index=0,
    key="age_income_country_filter"
)

# Filter dataset to selected scope
filtered_age_inc = age_inc_df[
    age_inc_df["Country"] == selected_view
].copy()

# 3. Enforce custom logical categorical sorting for both dimensions
income_order = [
    "0-25K",
    "25K-50K",
    "50K-75K",
    "75K-100K",
    "100K-125K",
    "125K+"
]

age_order = [
    "30 to 50",
    "51 to 60",
    "61 to 90",
    "Other"
]

filtered_age_inc["Income_Group"] = pd.Categorical(
    filtered_age_inc["Income_Group"],
    categories=income_order,
    ordered=True
)

filtered_age_inc["Age_Group"] = pd.Categorical(
    filtered_age_inc["Age_Group"],
    categories=age_order,
    ordered=True
)

filtered_age_inc = (
    filtered_age_inc
    .sort_values(by=["Income_Group", "Age_Group"])
    .reset_index(drop=True)
)

# 4. Generate the Grouped Column Chart
age_inc_fig = px.bar(
    filtered_age_inc,
    x="Income_Group",      # Income brackets on X-axis
    y="Customer_Count",    # Customer volume
    color="Age_Group",     # Age cohorts grouped within each income bracket
    barmode="group",
)

age_inc_fig.update_layout(
    xaxis_title="Income Bracket",
    yaxis_title="Customer Count",
    legend_title="Age Group",
    height=500
)

st.plotly_chart(age_inc_fig, width='stretch')

st.divider()

st.subheader("Education vs Income Distribution")

# 1. Fetch cross-tabulated dataset
edu_inc_query, edu_inc_params = get_education_vs_income_query()

edu_inc_df = pd.read_sql(
    edu_inc_query,
    engine,
    params=edu_inc_params
)

# 2. Dropdown filter to switch country focus
selected_edu_view = st.selectbox(
    "Select Country",
    options=list(edu_inc_df["Country"].unique()),
    index=0,
    key="edu_income_country_filter"
)

# Filter dataset to selected country focus
filtered_edu_inc = edu_inc_df[
    edu_inc_df["Country"] == selected_edu_view
].copy()

# 3. Enforce custom logical categorical sorting for the Income X-axis
income_order = [
    "0-25K",
    "25K-50K",
    "50K-75K",
    "75K-100K",
    "100K-125K",
    "125K+"
]

filtered_edu_inc["Income_Group"] = pd.Categorical(
    filtered_edu_inc["Income_Group"],
    categories=income_order,
    ordered=True
)

# Sort by Income Group and Education for clean visual grouping
filtered_edu_inc = (
    filtered_edu_inc
    .sort_values(by=["Income_Group", "Education"])
    .reset_index(drop=True)
)

# 4. Generate the Grouped Column Chart
edu_inc_fig = px.bar(
    filtered_edu_inc,
    x="Income_Group",          # Income brackets on X-axis
    y="Customer_Count",        # Customer volume on Y-axis
    color="Education",         # Grouped by education level
    barmode="group",
)

edu_inc_fig.update_layout(
    xaxis_title="Income Bracket",
    yaxis_title="Customer Count",
    legend_title="Education Level",
    height=500
)

st.plotly_chart(
    edu_inc_fig,
    width='stretch'
)

st.divider()

st.subheader("Marital Status vs Income Distrubution")

# 1. Fetch cross-tabulated dataset
mar_inc_query, mar_inc_params = get_marital_vs_income_query()

mar_inc_df = pd.read_sql(
    mar_inc_query,
    engine,
    params=mar_inc_params
)

# 2. Localized filter element to isolate geography focus
selected_mar_view = st.selectbox(
    "Select Country",
    options=list(mar_inc_df["Country"].unique()),
    index=0,
    key="mar_income_country_filter"
)

# Filter dataset to chosen scope
filtered_mar_inc = mar_inc_df[
    mar_inc_df["Country"] == selected_mar_view
].copy()

# 3. Enforce custom logical categorical sorting for the Income X-axis
income_order = [
    "0-25K",
    "25K-50K",
    "50K-75K",
    "75K-100K",
    "100K-125K",
    "125K+"
]

filtered_mar_inc["Income_Group"] = pd.Categorical(
    filtered_mar_inc["Income_Group"],
    categories=income_order,
    ordered=True
)

# Sort by Income Group and Marital Status for structured clustered column spacing
filtered_mar_inc = (
    filtered_mar_inc
    .sort_values(by=["Income_Group", "Marital_Status"])
    .reset_index(drop=True)
)

# 4. Generate the Grouped Column Chart
mar_inc_fig = px.bar(
    filtered_mar_inc,
    x="Income_Group",          # Income brackets on X-axis
    y="Customer_Count",        # Customer volume on Y-axis
    color="Marital_Status",    # Grouped by marital status
    barmode="group",
)

mar_inc_fig.update_layout(
    xaxis_title="Income Bracket",
    yaxis_title="Customer Count",
    legend_title="Marital Status",
    height=500
)

st.plotly_chart(
    mar_inc_fig,
    width='stretch'
)

st.divider()

st.subheader("Family Customer vs Income Distribution")

# 1. Fetch cross-tabulated dataset
fam_inc_query, fam_inc_params = get_family_vs_income_query()

fam_inc_df = pd.read_sql(
    fam_inc_query,
    engine,
    params=fam_inc_params
)

# 2. Localized filter element to isolate geography focus
selected_fam_view = st.selectbox(
    "Select Country",
    options=list(fam_inc_df["Country"].unique()),
    index=0,
    key="fam_income_country_filter"
)

# Filter dataset to chosen scope
filtered_fam_inc = fam_inc_df[
    fam_inc_df["Country"] == selected_fam_view
].copy()

# 3. Enforce custom logical categorical sorting for the Income X-axis
income_order = [
    "0-25K",
    "25K-50K",
    "50K-75K",
    "75K-100K",
    "100K-125K",
    "125K+"
]

filtered_fam_inc["Income_Group"] = pd.Categorical(
    filtered_fam_inc["Income_Group"],
    categories=income_order,
    ordered=True
)

# Sort by Income Group and Family Status for structured clustered column spacing
filtered_fam_inc = (
    filtered_fam_inc
    .sort_values(by=["Income_Group", "Family_Status"])
    .reset_index(drop=True)
)

# 4. Generate the Grouped Column Chart
fam_inc_fig = px.bar(
    filtered_fam_inc,
    x="Income_Group",         # Income brackets on X-axis
    y="Customer_Count",       # Customer volume on Y-axis
    color="Family_Status",    # Family vs Non-Family grouping
    barmode="group",
)

fam_inc_fig.update_layout(
    xaxis_title="Income Bracket",
    yaxis_title="Customer Count",
    legend_title="Household Status",
    height=500
)

st.plotly_chart(
    fam_inc_fig,
    width='stretch'
)