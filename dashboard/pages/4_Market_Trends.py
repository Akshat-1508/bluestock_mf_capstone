import pandas as pd
import streamlit as st
import plotly.express as px

from utils import get_filter_options, load_table

sip = load_table(
    "fact_monthly_sip_inflows"
)

category = load_table(
    "fact_category_inflows"
)

benchmark = load_table(
    "fact_benchmark_indices"
)

st.title(
    "SIP & Market Trends"
)

fig = px.line(
    sip,
    x="month",
    y="sip_inflow_crore"
)

st.plotly_chart(
    fig,
    width="stretch"
)

pivot = category.pivot(
    index="category",
    columns="month",
    values="net_inflow_crore"
)

fig2 = px.imshow(
    pivot,
    aspect="auto"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

nifty50 = benchmark[
    benchmark["index_name"]
    == "NIFTY50"
]

fig3 = px.line(
    nifty50,
    x="date",
    y="close_value"
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
benchmark = load_table("fact_benchmark_indices")

benchmark["date"] = pd.to_datetime(
    benchmark["date"]
)

fig = px.line(
    benchmark,
    x="date",
    y="close_value",
    color="index_name",
    title="Market Index Trends"
)

st.plotly_chart(fig, use_container_width=True)

benchmark = load_table(
    "fact_benchmark_indices"
)

fig = px.line(
    benchmark,
    x="date",
    y="close_value",
    color="index_name"
)

st.plotly_chart(fig)