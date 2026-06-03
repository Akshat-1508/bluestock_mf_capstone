# Bluestock Mutual Fund Analytics Data Dictionary

This document describes all datasets, columns, data types, and business definitions used in the project.

## dim_fund

Source: 01_fund_master.csv

| Column      | Type     | Description                |
|-------------|----------|----------------------------|
| amfi_code   | INTEGER  | Unique AMFI scheme code    |
| scheme_name | TEXT     | Name of mutual fund scheme |
| fund_house  | TEXT     | Asset management company   |
| category    | TEXT     | Equity, Debt, Hybrid etc.  |
| plan        | TEXT     | Direct or Regular plan     |


## fact_nav

Source: 02_nav_history.csv

| Column    | Type    | Description                   |
|-----------|---------|-------------------------------|
| amfi_code | INTEGER | Mutual fund scheme identifier |
| date      | DATE    | NAV date                      |
| nav       | REAL    | Net Asset Value               |

## fact_transactions

Source: 08_investor_transactions.csv

| Column           | Type    | Description                  |
|------------------|---------|------------------------------|
| investor_id      | INTEGER | Unique investor identifier   |
| transaction_date | DATE    | Date of transaction          |
| amfi_code        | INTEGER | Mutual fund scheme code      |
| transaction_type | TEXT    | SIP, Lumpsum or Redemption   |
| amount_inr       | REAL    | Transaction amount in INR    |
| state            | TEXT    | Investor state               |
| city             | TEXT    | Investor city                |
| city_tier        | TEXT    | Tier 1,Tier 2 or Tier 3 city |
| age_group        | TEXT    | Investor age category        |
| gender           | TEXT    | Investor gender              |
| annualincomelakh | REAL    | Annual income in lakh rupees |
| payment_mode     | TEXT    | UPI, Net Banking, Card etc.  |
| kyc_status       | TEXT    | KYC verification status      |

## fact_performance

Source: 07_scheme_performance.csv

| Column             | Type    | Description                         |
|--------------------|---------|-------------------------------------|
| amfi_code          | INTEGER | Scheme identifier                   | 
| fund_house         | TEXT    | AMC name                            |
| scheme_name        | TEXT    | Mutual fund scheme                  |
| category           | TEXT    | Fund category                       |
| plan               | TEXT    | Direct or Regular                   |
| return_1yr_pct     | REAL    | One year return percentage          |
| return_3yr_pct     | REAL    | Three year return percentage        |
| return_5yr_pct     | REAL    | Five year return percentage         | 
| benchmark_3yr_pct  | REAL    | Benchmark return percentage         |
| alpha              | REAL    | Alpha performance metric            |
| beta               | REAL    | Beta risk metric                    |
| sharpe_ratio       | REAL    | Risk adjusted return metric         |
| sortino_ratio      | REAL    | Downside risk adjusted return       |
| std_dev_ann_pct    | REAL    | Annualized standard deviation       |
| max_drawdown_pct   | REAL    | Maximum drawdown percentage         |
| aum_crore          | REAL    | Assets Under Management (Crore INR) |
| expense_ratio_pct  | REAL    | Expense ratio percentage            |
| morningstar_rating | INTEGER | Rating from 1 to 5                  |
| risk_grade         | TEXT    | Risk classification                 | 