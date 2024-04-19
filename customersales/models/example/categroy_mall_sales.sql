SELECT 
    YEAR(invoice_date) as year, 
    MONTH(invoice_date) as month,
    SUM(quantity * price) as total_sales, 
    shopping_mall
FROM 
    {{ ref('annual_mall_earnings') }}
GROUP BY 
    YEAR(invoice_date), 
    MONTH(invoice_date), 
    shopping_mall
ORDER BY 
    total_sales DESC;
