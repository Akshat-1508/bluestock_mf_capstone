# src/data_ingestion.py

from pathlib import Path
import pandas as pd

RAW_PATH = Path("data/raw")

for file in RAW_PATH.glob("*.csv"):
    df = pd.read_csv(file)

    print("\n", "="*50)
    print(file.name)
    print(df.shape)
    print(df.dtypes)
    print(df.head())

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