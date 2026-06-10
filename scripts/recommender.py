import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = (
    BASE_DIR
    / "data"
    / "db"
    / "bluestock_mf.db"
)

conn = sqlite3.connect(DB_PATH)

df = pd.read_sql(
    "SELECT * FROM fact_performance",
    conn
)

conn.close()

# ==========================================
# USER INPUT
# ==========================================

print("\n" + "="*60)
print("BLUESTOCK FUND RECOMMENDATION ENGINE")
print("="*60)

risk = input(
    "\nEnter Risk Appetite (Low / Moderate / High): "
).strip().lower()

# ==========================================
# RISK MAPPING
# ==========================================

if risk == "low":

    filtered = df[
        df["risk_grade"] == "Low"
    ].copy()

elif risk == "moderate":

    filtered = df[
        df["risk_grade"].isin(
            [
                "Moderate",
                "Moderately High"
            ]
        )
    ].copy()

elif risk == "high":

    filtered = df[
        df["risk_grade"].isin(
            [
                "High",
                "Very High"
            ]
        )
    ].copy()

else:

    print("\nInvalid Risk Appetite!")
    print("Please enter: Low, Moderate or High")
    exit()

# ==========================================
# RECOMMENDATION SCORE
# ==========================================

filtered["recommendation_score"] = (
      0.35 * filtered["sharpe_ratio"]
    + 0.25 * filtered["sortino_ratio"]
    + 0.20 * filtered["alpha"]
    + 0.20 * filtered["return_3yr_pct"]
)

# ==========================================
# TOP 3 RECOMMENDATIONS
# ==========================================

recommendations = (
    filtered
    .sort_values(
        "recommendation_score",
        ascending=False
    )
    .head(3)
)

# ==========================================
# DISPLAY RESULTS
# ==========================================

print("\n")
print("="*80)
print("TOP 3 RECOMMENDED FUNDS")
print("="*80)

print(
    recommendations[
        [
            "scheme_name",
            "fund_house",
            "risk_grade",
            "return_3yr_pct",
            "sharpe_ratio",
            "sortino_ratio",
            "alpha",
            "recommendation_score"
        ]
    ].to_string(index=False)
)

# ==========================================
# BEST MATCH
# ==========================================

best = recommendations.iloc[0]

print("\n")
print("="*80)
print("BEST MATCH")
print("="*80)

print(
    f"""
Fund Name     : {best['scheme_name']}
Fund House    : {best['fund_house']}
Risk Grade    : {best['risk_grade']}
3Y Return     : {best['return_3yr_pct']:.2f}%
Sharpe Ratio  : {best['sharpe_ratio']:.2f}
Sortino Ratio : {best['sortino_ratio']:.2f}
Alpha         : {best['alpha']:.2f}
Score         : {best['recommendation_score']:.2f}
"""
)

# ==========================================
# SAVE RECOMMENDATIONS
# ==========================================
OUTPUT_DIR = (
    BASE_DIR
    / "reports"
    / "During_Internship"
    / "Day-06"
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


recommendations.to_csv(
    OUTPUT_DIR / "recommendations.csv",
    index=False
)

print("="*80)
print("Recommendations saved successfully:")
print(
    "../reports/During_Internship/Day-06/recommended_funds.csv"
)
print("="*80)

