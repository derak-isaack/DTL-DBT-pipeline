SELECT YEAR(invoice_date) as year, SUM(quantity*price) as total_sales, shopping_mall
FROM customer_shopping_data
GROUP BY shopping_mall, year
ORDER BY total_sales DESC