import streamlit as st
from PIL import Image
from pathlib import Path

# =====================================
# PAGE CONFIG (MUST BE FIRST STREAMLIT COMMAND)
# =====================================

st.set_page_config(
    page_title="Bluestock MF Analytics",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================
# PATHS
# =====================================

BASE_DIR = Path(__file__).resolve().parent

logo_path = BASE_DIR / "assets" / "bluestock_logo.png"
css_path = BASE_DIR / "style.css"

# =====================================
# HIDE STREAMLIT DEFAULT UI
# =====================================

hide_st_style = """
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""

st.markdown(hide_st_style, unsafe_allow_html=True)

# =====================================
# LOAD CUSTOM CSS
# =====================================

if css_path.exists():
    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:


    st.markdown("## 📊 Dashboard Navigation")

    st.info(
        """
        Use the sidebar to explore:

        • Industry Overview

        • Fund Performance

        • Investor Analytics

        • Market Trends
        """
    )

    st.markdown("---")

    st.caption(
        "Bluestock Internship Project"
    )

# =====================================
# MAIN HEADER
# =====================================

st.markdown("""
<div style="
background: linear-gradient(135deg,#5B4DFF,#7B61FF);
padding:25px;
border-radius:18px;
margin-bottom:25px;
box-shadow:0px 4px 20px rgba(91,77,255,0.35);
">

<h1 style="
color:white;
margin:0;
font-size:42px;
">
📈 Bluestock Mutual Fund Analytics Dashboard
</h1>

<p style="
color:white;
font-size:18px;
margin-top:10px;
">
Analyze Mutual Fund Performance, Investor Behaviour,
SIP Trends, Portfolio Allocations and Market Benchmarks
</p>

</div>
""", unsafe_allow_html=True)

# =====================================
# WELCOME SECTION
# =====================================

st.markdown("## Welcome")

st.markdown("""
This dashboard was developed as part of the **Bluestock Mutual Fund Analytics Internship Project**.

The platform provides insights into:

- 📊 Mutual Fund Performance
- 💰 SIP Growth Trends
- 🏦 Fund House Analysis
- 👥 Investor Demographics
- 📈 Market Benchmarks
- 🎯 Fund Scorecards
""")

# =====================================
# QUICK SNAPSHOT
# =====================================

st.markdown("## Quick Dashboard Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.success("📈 Performance Analytics")

with col2:
    st.info("💰 SIP Insights")

with col3:
    st.warning("🏦 Fund Houses")

with col4:
    st.error("📊 Market Benchmarks")

# =====================================
# FEATURE CARDS
# =====================================

st.markdown("## Available Dashboard Pages")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    ### 🏦 Industry Overview

    - Industry AUM
    - Fund Houses
    - SIP Growth
    - Folio Analysis
    """)

    st.markdown("""
    ### 📈 Fund Performance

    - Risk vs Return
    - Sharpe Ratio
    - Alpha/Beta
    - Fund Scorecards
    """)

with col2:

    st.markdown("""
    ### 👥 Investor Analytics

    - State Analysis
    - Gender Distribution
    - Age Groups
    - T30 vs B30
    """)

    st.markdown("""
    ### 🌍 Market Trends

    - SIP Trends
    - Category Inflows
    - Benchmark Analysis
    - Sector Allocation
    """)

# =====================================
# FOOTER
# =====================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div style="
background: linear-gradient(135deg,#5B4DFF,#7B61FF);
padding:25px;
border-radius:18px;
text-align:center;
margin-top:30px;
box-shadow:0px 4px 20px rgba(91,77,255,0.35);
">

<h2 style="
color:white;
margin-bottom:10px;
">
📊 Bluestock Mutual Fund Analytics
</h2>

<p style="
color:white;
font-size:16px;
">
Interactive Dashboard for Mutual Fund Performance,
Investor Analytics, SIP Trends and Market Insights
</p>

<hr style="
border:1px solid rgba(255,255,255,0.3);
">

<p style="
color:#F3F4F6;
font-size:15px;
">
🚀 Built with Streamlit • Python • SQLite • Plotly
</p>

<p style="
color:#F3F4F6;
font-size:14px;
">
Bluestock Internship Program 2025
</p>

<p style="
color:#F3F4F6;
font-size:14px;
">
Designed & Developed by <b>Akshat Bansal</b>
</p>

</div>
""", unsafe_allow_html=True)