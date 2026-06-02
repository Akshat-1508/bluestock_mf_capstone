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