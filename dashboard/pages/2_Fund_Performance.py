import pandas as pd
import streamlit as st
import plotly.express as px
from pathlib import Path
from utils import get_filter_options, load_table

perf = load_table("fact_performance")

st.title("Fund Performance")

category = st.sidebar.multiselect(
    "Category",
    perf["category"].unique()
)

if category:
    perf = perf[
        perf["category"].isin(category)
    ]

fig = px.scatter(
    perf,
    x="return_3yr_pct",
    y="sharpe_ratio",
    size="aum_crore",
    color="category",
    hover_name="scheme_name",
    hover_data=[
        "fund_house",
        "return_5yr_pct",
        "alpha",
        "beta"
    ]
)
st.plotly_chart(
    fig,
    width="stretch"
)
st.subheader("Fund Scorecard")

show_cols = [
    "scheme_name",
    "return_3yr_pct",
    "sharpe_ratio",
    "alpha",
    "expense_ratio_pct"
]

st.dataframe(
    perf[show_cols]
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
BASE_DIR = Path(__file__).resolve().parents[2]

scorecard_path = (
    BASE_DIR
    / "reports"
    / "During_Internship"
    / "Day-04"
    / "fund_scorecard.csv"
)

scorecard = pd.read_csv(scorecard_path)

st.subheader("Top 10 Funds")

st.dataframe(
    scorecard.sort_values(
        "fund_score",
        ascending=False
    ).head(10)
)
st.subheader("Bottom 10 Funds")

st.dataframe(
    scorecard.sort_values(
        "fund_score"
    ).head(10)
)
benchmark = load_table(
    "fact_benchmark_indices"
)

nav = load_table(
    "fact_nav"
)
import plotly.express as px

fig = px.line(
    benchmark,
    x="date",
    y="close_value",
    color="index_name",
    title="Benchmark Comparison"
)

st.plotly_chart(fig)

selected_fund = st.selectbox(
    "Select Fund",
    sorted(perf["scheme_name"].unique())
)
fund_data = perf[
    perf["scheme_name"] == selected_fund
]

st.dataframe(fund_data)


st.download_button(
    "Download Data",
    perf.to_csv(index=False),
    "performance.csv",
    "text/csv"
)