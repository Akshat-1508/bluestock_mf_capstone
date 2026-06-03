# src/data_ingestion.py

# from pathlib import Path
# import pandas as pd

# RAW_PATH = Path("data/raw")

# for file in RAW_PATH.glob("*.csv"):
#     df = pd.read_csv(file)

#     print("\n", "="*50)
#     print(file.name)
#     print(df.shape)
#     print(df.dtypes)
#     print(df.head())

from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///data/db/bluestock_mf.db"
)

import sqlite3

conn = sqlite3.connect(
    "data/db/bluestock_mf.db"
)

conn.close()

print("Database Created")
import pandas as pd
nav = pd.read_csv(
    "data/processed/clean_nav_history.csv"
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

txn = pd.read_csv(
    "data/processed/clean_transactions.csv"
)

txn.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf = pd.read_csv(
    "data/processed/clean_performance.csv"
)

perf.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

fun = pd.read_csv(
    "data/processed/clean_01_fund_master.csv"
)

fun.to_sql(
    "fact_fund_master",
    engine,
    if_exists="replace",
    index=False
)

aum = pd.read_csv(
    "data/processed/clean_03_aum_by_fund_house.csv"
)

aum.to_sql(
    "fact_aum_house",
    engine,
    if_exists="replace",
    index=False
)

monh = pd.read_csv(
    "data/processed/clean_04_monthly_sip_inflows.csv"
)

monh.to_sql(
    "fact_monthly_sip_inflows",
    engine,
    if_exists="replace",
    index=False
)

cat = pd.read_csv(
    "data/processed/clean_05_category_inflows.csv"
)

cat.to_sql(
    "fact_category_inflows",
    engine,
    if_exists="replace",
    index=False
)

ind = pd.read_csv(
    "data/processed/clean_06_industry_folio_count.csv"
)

ind.to_sql(
    "fact_industry_folio_count",
    engine,
    if_exists="replace",
    index=False
)

port = pd.read_csv(
    "data/processed/clean_09_portfolio_holdings.csv"
)

port.to_sql(
    "fact_portfolio_holdings",
    engine,
    if_exists="replace",
    index=False
)


bench = pd.read_csv(
    "data/processed/clean_10_benchmark_indices.csv"
)

bench.to_sql(
    "fact_benchmark_indices",
    engine,
    if_exists="replace",
    index=False
)


