import pandas as pd

# read in the sales data from the CSV file
sales_data = pd.read_csv('sales_dataset.csv')

# calculate the total sales for each product
product_sales = sales_data.groupby('Product Name')['Sale Price'].sum()

# determine the average sale price for each product category
category_avg_price = sales_data.groupby('Category')['Sale Price'].mean()

# identify the month with the highest sales and the month with the lowest sales
month_sales = sales_data.groupby('Month')['Sale Price'].sum()
highest_month = month_sales.idxmax()
lowest_month = month_sales.idxmin()

# determine which customers made the most purchases and how much they spent in total
customer_sales = sales_data.groupby('Customer Name')['Sale Price'].sum()
top_customers = customer_sales.nlargest(5)

# write the results to a CSV file
product_sales.to_csv('product_sales.csv')
category_avg_price.to_csv('category_avg_price.csv')
top_customers.to_csv('top_customers.csv')

# print the results
print('Total sales by product:')
print(product_sales)
print('\nAverage sale price by category:')
print(category_avg_price)
print('\nMonth with highest sales:', highest_month)
print('Month with lowest sales:', lowest_month)
print('\nTop customers by total spending:')
print(top_customers)