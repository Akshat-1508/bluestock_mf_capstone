import streamlit as st
import plotly.express as px

from utils import get_filter_options, load_table

aum = load_table("fact_aum_house")
folio = load_table("fact_industry_folio_count")
sip = load_table("fact_monthly_sip_inflows")
fund = load_table("fact_fund_master")

st.title("Industry Overview")
col1,col2,col3,col4 = st.columns(4)
col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric(
        "Industry AUM",
        "₹68.1 L Cr",
        "+12%"
    )

with col2:
    st.metric(
        "Monthly SIP",
        "₹31K Cr",
        "+8%"
    )

with col3:
    st.metric(
        "Total Folios",
        "26.12 Cr",
        "+97%"
    )

with col4:
    st.metric(
        "Schemes",
        "1980",
        "+4%"
    )
col1.metric(
    "Fund Houses",
    aum["fund_house"].nunique()
)

col2.metric(
    "Schemes",
    fund["amfi_code"].nunique()
)

col3.metric(
    "Latest SIP (Cr)",
    round(
        sip["sip_inflow_crore"].iloc[-1],
        2
    )
)

col4.metric(
    "Folios (Cr)",
    round(
        folio["total_folios_crore"].iloc[-1],
        2
    )
)

st.subheader("Industry Snapshot")

col1,col2,col3 = st.columns(3)

col1.success("📈 Industry Growing")
col2.info("💰 SIP Record High")
col3.warning("⚠️ Midcap Valuations Elevated")

st.subheader("AUM Growth")

fig = px.line(
    aum,
    x="date",
    y="aum_lakh_crore",
    color="fund_house"
)

st.plotly_chart(
    fig,
    width="stretch"
)

st.subheader("Top Fund Houses")

latest = aum.sort_values(
    "date"
).groupby(
    "fund_house"
).tail(1)

top10 = latest.nlargest(
    10,
    "aum_lakh_crore"
)

fig2 = px.bar(
    top10,
    x="fund_house",
    y="aum_lakh_crore"
)


st.plotly_chart(
    fig2,
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

st.download_button(
    "Download Aum House Data",
    aum.to_csv(index=False),
    "performance.csv",
    "text/csv"
)

st.download_button(
    "Download Industry Folio Count Data",
    folio.to_csv(index=False),
    "performance.csv",
    "text/csv"
)
