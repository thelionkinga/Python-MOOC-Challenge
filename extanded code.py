import pandas as pd

# read in sales data from CSV file
df = pd.read_csv('sales_dataset.csv')

# calculate total sales for each product
total_sales = df.groupby('Product Name')['Quantity Sold'].sum().reset_index()

# determine average sale price for each product category
avg_price = df.groupby('Category')['Sale Price'].mean().reset_index()

# identify month with highest and lowest sales
monthly_sales = df.groupby('Month')['Quantity Sold'].sum().reset_index()
max_month = monthly_sales.loc[monthly_sales['Quantity Sold'].idxmax()]
min_month = monthly_sales.loc[monthly_sales['Quantity Sold'].idxmin()]

# determine which customers made the most purchases and how much they spent in total
customer_sales = df.groupby('Customer Name')['Sale Price'].sum().reset_index()
top_customer = customer_sales.loc[customer_sales['Sale Price'].idxmax()]

# calculate additional metrics
median_price = df.groupby('Product Name')['Sale Price'].median().reset_index()
std_dev_price = df.groupby('Product Name')['Sale Price'].std().reset_index()

# print results
print("Total sales for each product:")
print(total_sales)
print("\nAverage sale price for each product category:")
print(avg_price)
print("\nMonth with the highest sales:")
print(max_month['Month'], "with", max_month['Quantity Sold'], "units sold")
print("\nMonth with the lowest sales:")
print(min_month['Month'], "with", min_month['Quantity Sold'], "units sold")
print("\nTop customer by sales:")
print(top_customer['Customer Name'], "with $", round(top_customer['Sale Price'], 2), "in sales")
print("\nMedian sale price for each product:")
print(median_price)
print("\nStandard deviation of sale prices for each product:")
print(std_dev_price)