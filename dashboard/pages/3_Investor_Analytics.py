import streamlit as st
import plotly.express as px

from utils import get_filter_options, load_table

txn = load_table(
    "fact_transactions"
)

st.title(
    "Investor Analytics"
)

state = st.sidebar.multiselect(
    "State",
    txn["state"].unique()
)

if state:
    txn = txn[
        txn["state"].isin(state)
    ]

state_amt = (
    txn.groupby("state")
    ["amount_inr"]
    .sum()
    .reset_index()
)

fig = px.bar(
    state_amt,
    x="amount_inr",
    y="state",
    orientation="h"
)


st.plotly_chart(
    fig,
    width="stretch"
)

gender = (
    txn["gender"]
    .value_counts()
    .reset_index()
)

fig2 = px.pie(
    gender,
    names="gender"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

fig3 = px.box(
    txn,
    x="age_group",
    y="amount_inr"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

filters = get_filter_options()

selected_house = st.sidebar.selectbox(
    "Fund House",
    ["All"] + filters["fund_house"]
)

selected_category = st.sidebar.selectbox(
    "Category",
    ["All"] + filters["category"]
)

selected_plan = st.sidebar.selectbox(
    "Plan",
    ["All"] + filters["plan"]
)

txn = load_table("fact_transactions")
tier_counts = (
    txn["city_tier"]
    .value_counts()
    .reset_index()
)

tier_counts.columns = [
    "city_tier",
    "count"
]
import plotly.express as px

fig = px.pie(
    tier_counts,
    names="city_tier",
    values="count",
    hole=0.5,
    title="T30 vs B30 Investors"
)


st.plotly_chart(fig)

gender = (
    txn.groupby("gender")
    .size()
    .reset_index(name="count")
)

fig = px.pie(
    gender,
    names="gender",
    values="count",
    hole=0.5
)

st.plotly_chart(fig)

tier = (
    txn.groupby("city_tier")
    .size()
    .reset_index(name="count")
)

fig = px.pie(
    tier,
    names="city_tier",
    values="count",
    hole=0.5
)

st.plotly_chart(fig)

st.download_button(
    "Download Transactions Data",
    txn.to_csv(index=False),
    "performance.csv",
    "text/csv"
)