SELECT
amfi_code,
aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

SELECT AVG(nav) AS avg_nav
FROM fact_nav;

SELECT
    strftime('%Y-%m', nav_date) AS month,
    AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

SELECT
    transaction_type,
    COUNT(*) AS total
FROM fact_transactions
GROUP BY transaction_type;

SELECT
    state,
    COUNT(*) AS total
FROM fact_transactions
GROUP BY state
ORDER BY total DESC;

SELECT
    amfi_code,
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

SELECT
    amfi_code,
    scheme_name,
    sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

SELECT
    amfi_code,
    scheme_name,
    return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 10;

SELECT
    AVG(expense_ratio_pct) AS avg_expense_ratio
FROM fact_performance;


SELECT
    amfi_code,
    scheme_name,
    sharpe_ratio
FROM fact_performance
WHERE sharpe_ratio < 0;