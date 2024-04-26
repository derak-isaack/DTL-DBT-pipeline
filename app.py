import duckdb
import streamlit as st  
import pandas as pd
import plotly.express as px





st.set_page_config(page_title="Shopping mall sales dashboard",
                    layout="wide",
                    page_icon=":bar_chart:",
                    )


input_file = 'standard_filesystem2.duckdb'
database = duckdb.connect(database=input_file)

query_1 = database.query("SELECT * FROM customer_shopping_data.customer_data").to_df()

# st.dataframe(query_1)
#Convert invoice date to year
query_1['year'] = query_1['invoice_date'].dt.year.astype(int)
#Convert invoice date to month
query_1['month'] = query_1['invoice_date'].dt.month.astype(int)
# #Convert invoice date to week
# query_1['week'] = query_1['invoice_date'].dt.week

# Create new column for total sales
query_1['total_sales'] = query_1['quantity'] * query_1['price']

st.sidebar.header("Filter data here:")
#Filter for mall name
mall = st.sidebar.multiselect(
                            "Select the mall:", 
                            options = query_1["shopping_mall"].unique(),
                            default = query_1["shopping_mall"].unique()
)  
#Filter for product category
product_category = st.sidebar.multiselect(
                            "Select the product category:", 
                            options = query_1["category"].unique(),
                            default = query_1["category"].unique()
)  
#Filter for gender
gender_select = st.sidebar.multiselect(
                            "Select the gender:", 
                            options = query_1["gender"].unique(),
                            default = query_1["gender"].unique()
)  
#define filter for payment method
shoppers_payment_method = st.sidebar.multiselect(
                            "Select the payment method:",
                            options = query_1["payment_method"].unique(),
                            default = query_1["payment_method"].unique()
) 
select_year = st.sidebar.multiselect(
                            "Select the year:", 
                            options=query_1['year'].unique(), 
                            default=query_1['year'].unique() 
)
select_month = st.sidebar.multiselect(
                            "Select the month:",
                            options=query_1['month'].unique(),
                            default=query_1['month'].unique()
)

#Refer the filters to original dataframe columns
data_query = query_1.query(
    "shopping_mall==@mall & category==@product_category & gender==@gender_select & payment_method==@shoppers_payment_method & year==@select_year & month==@select_month"
)

# st.dataframe(data_query)


st.title(":bar_chart: Shopping mall sales dashboard")
st.markdown("##")

# Key Performance Indicators
totalsales = int(data_query["total_sales"].sum())


columns = st.columns(1)

# Display the total sales in the left column
with columns[0]:
    st.subheader("Total sales:")
    st.subheader(f"${totalsales:,}")
    
st.markdown("---")


sales_by_mall = (
    data_query.groupby("shopping_mall")['total_sales'].agg('sum').sort_values(ascending=False)
    )
fig_sales = px.bar(
    sales_by_mall.reset_index(),
    x="total_sales",
    y='shopping_mall',
    # This creates a horizontal bar chart.
    orientation="h",
    title="<b>Sales by mall</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_mall),
    template="plotly_white",
)
# st.plotly_chart(fig_sales) 

mall_category_totals = (
                    data_query.groupby(["category"])["quantity"].agg('sum').sort_values(ascending=False)
)
fig_category = px.bar(
    mall_category_totals.reset_index(),
    x="category",
    y='quantity',
    # This creates a vertical bar chart.    
    orientation="v",
    title="<b>Total quantity of products sold</b>",
    color_discrete_sequence=["#0083B8"] * len(mall_category_totals),
    template="plotly_white",
)
# st.plotly_chart(fig_category)
left_column, right_column = st.columns(2)

# Display the charts in left and right columns.
left_column.plotly_chart(fig_sales, use_container_width=True)
right_column.plotly_chart(fig_category, use_container_width=True)