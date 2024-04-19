SELECT YEAR(invoice_date) AS year,
        MONTH(invoice_date) as month, 
        quantity*price as total_sales, shopping_mall
FROM read_csv_duckdb
GROUP BY year, shopping_mall, month
ORDER BY total_sales DESC;