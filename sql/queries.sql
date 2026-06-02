SELECT
amfi_code,
aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;