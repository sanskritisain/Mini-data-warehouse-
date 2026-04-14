import pandas as pd
import sqlite3

print("🚀 Data Warehouse Process Started")

# ------------------ EXTRACT ------------------
df = pd.read_csv("data/sales.csv")

print("Original Data:")
print(df.head())

# ------------------ TRANSFORM ------------------

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Remove null values
df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

# ------------------ CREATE DIMENSIONS ------------------

# Customers table
customers = df[['customer_id', 'customer_name', 'city']].drop_duplicates()

# Products table
products = df[['product_id', 'product_name', 'category']].drop_duplicates()

# Fact table
sales = df[['order_id', 'customer_id', 'product_id', 'sales']]

# ------------------ LOAD ------------------
conn = sqlite3.connect("db/warehouse.db")

customers.to_sql("customers", conn, if_exists="replace", index=False)
products.to_sql("products", conn, if_exists="replace", index=False)
sales.to_sql("sales", conn, if_exists="replace", index=False)

print("✅ Data Loaded Successfully")

# ------------------ ANALYSIS ------------------

query = """
SELECT c.customer_name, p.product_name, s.sales
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id
JOIN products p ON s.product_id = p.product_id
LIMIT 10;
"""

result = pd.read_sql(query, conn)

print("Sample Data:")
print(result)

conn.close()