import requests
import pandas as pd
from pathlib import Path

schemes = {
    119551: "SBI_Bluechip",
    120503: "ICICI_Bluechip",
    118632: "Nippon_LargeCap",
    119092: "Axis_Bluechip",
    120841: "Kotak_Bluechip"
}

raw_path = Path("data/raw")

for code, name in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    nav_df.to_csv(
        raw_path / f"{name}.csv",
        index=False
    )

    print(f"{name} saved successfully")