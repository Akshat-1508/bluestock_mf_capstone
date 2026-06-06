from pathlib import Path
import sqlite3
import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "data" / "db" / "bluestock_mf.db"



def load_table(table_name):

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql(
        f"SELECT * FROM {table_name}",
        conn
    )

    conn.close()

    return df

def get_filter_options():
    fund_master = load_table("fact_fund_master")

    return {
        "fund_house": sorted(
            fund_master["fund_house"].dropna().unique()
        ),
        "category": sorted(
            fund_master["category"].dropna().unique()
        ),
        "plan": sorted(
            fund_master["plan"].dropna().unique()
        )
    }