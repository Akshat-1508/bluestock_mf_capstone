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


# clean_01_fund_master.csv

| Column Name        | Data Type | Description                            |
|--------------------|-----------|----------------------------------------|
| amfi_code          | INTEGER   | Unique AMFI scheme identifier          |
| fund_house         | TEXT      | Mutual fund company name               |
| scheme_name        | TEXT      | Name of the mutual fund scheme         |
| category           | TEXT      | Primary scheme category                |
| sub_category       | TEXT      | Detailed scheme category               |
| plan               | TEXT      | Regular or Direct plan                 |
| launch_date        | DATE      | Scheme launch date                     |
| benchmark          | TEXT      | Benchmark index used for comparison    |
| expense_ratio_pct  | REAL      | Annual expense ratio (%)               |
| exit_load_pct      | REAL      | Exit load charged on redemption (%)    |
| min_sip_amount     | REAL      | Minimum SIP investment amount (INR)    |
| min_lumpsum_amount | REAL      | Minimum lumpsum investment amount(INR) |
| fund_manager       | TEXT      | Fund manager name                      |
| risk_category      | TEXT      | Risk classification of scheme          |
| sebi_category_code | TEXT      | SEBI assigned category code            |

Source: AMFI Fund Master Dataset

---

# clean_03_aum_by_fund_house.csv

| Column Name    | Data Type | Description                          |
|----------------|-----------|--------------------------------------|
| date           | DATE      | Reporting date                       |  
| fund_house     | TEXT      | Mutual fund company                  |
| aum_lakh_crore | REAL      | Assets under management (Lakh Crore) |
| aum_crore      | REAL      | Assets under management (Crore)      |
| num_schemes    | INTEGER   | Number of active schemes             |

Source: AMFI AUM Reports

---

# clean_04_monthly_sip_inflows.csv

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| month | DATE | Monthly reporting period |
| sip_inflow_crore | REAL | Total SIP inflows (Crore INR) |
| active_sip_accounts_crore | REAL | Active SIP accounts (Crore) |
| new_sip_accounts_lakh | REAL | New SIP registrations (Lakh) |
| sip_aum_lakh_crore | REAL | SIP assets under management |
| yoy_growth_pct | REAL | Year-over-year SIP growth (%) |

Source: AMFI SIP Industry Data

---

# clean_05_category_inflows.csv

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| month | DATE | Monthly reporting period |
| category | TEXT | Mutual fund category |
| net_inflow_crore | REAL | Net inflow/outflow amount (Crore INR) |

Source: AMFI Category Flow Data

---

# clean_06_industry_folio_count.csv

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| month | DATE | Reporting month |
| total_folios_crore | REAL | Total investor folios |
| equity_folios_crore | REAL | Equity scheme folios |
| debt_folios_crore | REAL | Debt scheme folios |
| hybrid_folios_crore | REAL | Hybrid scheme folios |
| others_folios_crore | REAL | Other category folios |

Source: AMFI Industry Statistics

---

# clean_09_portfolio_holdings.csv

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| amfi_code | INTEGER | Mutual fund scheme identifier |
| stock_symbol | TEXT | NSE/BSE stock symbol |
| stock_name | TEXT | Company name |
| sector | TEXT | Industry sector |
| weight_pct | REAL | Portfolio allocation (%) |
| market_value_cr | REAL | Market value of holding (Crore INR) |
| current_price_inr | REAL | Current stock price (INR) |
| portfolio_date | DATE | Portfolio disclosure date |

Source: Fund Portfolio Disclosure Data

---

# clean_10_benchmark_indices.csv

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| date | DATE | Trading date |
| index_name | TEXT | Benchmark index name |
| close_value | REAL | Closing index value |
| daily_return_pct | REAL | Daily percentage return |

Source: NSE Benchmark Index Data

---

## Notes

- Monetary values are represented in Crore INR unless otherwise specified.
- Dates are stored in ISO format (YYYY-MM-DD).
- AMFI Code uniquely identifies each mutual fund scheme.
- Negative values in net_inflow_crore indicate net outflows.
- daily_return_pct is calculated during the data cleaning process.
- AUM units are explicitly maintained to avoid confusion between Crore and Lakh Crore values.
