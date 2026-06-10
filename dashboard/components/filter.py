import streamlit as st
from utils import get_filter_options

def sidebar_filters():

    filters = get_filter_options()

    st.sidebar.markdown("## 🎯 Filters")

    fund_house = st.sidebar.selectbox(
        "Fund House",
        ["All"] + filters["fund_house"]
    )

    category = st.sidebar.selectbox(
        "Category",
        ["All"] + filters["category"]
    )

    plan = st.sidebar.selectbox(
        "Plan",
        ["All"] + filters["plan"]
    )

    return fund_house, category, plan