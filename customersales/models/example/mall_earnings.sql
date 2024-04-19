
-- Use the `ref` function to select from other models

select avg(quantity * price) as total_avg_price, category, shopping_mall
from read_csv_duckdb
GROUP BY category, shopping_mall
ORDER BY total_avg_price DESC;

-- get the average price earned by various malls for each category   