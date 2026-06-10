import streamlit as st

def dashboard_metrics():

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
            "Folios",
            "26.12 Cr",
            "+97%"
        )

    with col4:
        st.metric(
            "Schemes",
            "1980",
            "+4%"
        )