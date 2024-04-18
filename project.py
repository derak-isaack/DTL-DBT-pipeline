import duckdb

input_file = "D:\\Projects\\AWS-S3 ETL\\standard_filesystem2.duckdb"
def run_queries_and_aggregations(input_file):
    # Connect to the DuckDB database file
    conn = duckdb.connect(database=input_file)

    # Execute SQL queries for analysis
    query_1 = "SELECT COUNT(*) AS total_rows FROM customer_shopping_data"
    query_2 = "SELECT category, SUM(quantity*price) AS total_sales FROM customer_shopping_data GROUP BY category"

    # Execute query 1
    result_1 = conn.execute(query_1)
    total_rows = result_1.fetchone()[0]
    print(f"Total rows in my_table: {total_rows}")

    # Execute query 2
    result_2 = conn.execute(query_2)
    print("Category-wise total sales:")
    for row in result_2.fetchall():
        category, total_sales = row
        print(f"{category}: {total_sales}")

    # Close the connection
    conn.close()

if __name__ == "__main__":

    # Run queries and aggregations on the data
    run_queries_and_aggregations(input_file)
  
