import streamlit as st
import pandas as pd
import sqlite3

st.title("📊 Mini Data Warehouse Dashboard")

# Upload file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Raw Data Preview")
    st.dataframe(df.head())

    # ------------------ CLEANING ------------------
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    st.write("Detected Columns:", list(df.columns))

    # ------------------ COLUMN SELECTION ------------------
    st.subheader("🛠️ Map Your Columns")

    customer_col = st.selectbox("Select Customer Column", df.columns)
    product_col = st.selectbox("Select Product Column", df.columns)
    sales_col = st.selectbox("Select Sales Column", df.columns)
    category_col = st.selectbox("Select Category Column (optional)", ["None"] + list(df.columns))

    # ------------------ PROCESS BUTTON ------------------
    if st.button("🚀 Process Data"):

        # Remove nulls & duplicates
        df = df.dropna()
        df = df.drop_duplicates()

        # Create IDs
        df["customer_id"] = df[customer_col].astype("category").cat.codes
        df["product_id"] = df[product_col].astype("category").cat.codes

        # ------------------ TABLES ------------------
        customers = df[["customer_id", customer_col]].drop_duplicates()
        customers.columns = ["customer_id", "customer_name"]

        if category_col != "None":
            products = df[["product_id", product_col, category_col]].drop_duplicates()
            products.columns = ["product_id", "product_name", "category"]
        else:
            products = df[["product_id", product_col]].drop_duplicates()
            products.columns = ["product_id", "product_name"]

        sales = df[["customer_id", "product_id", sales_col]]
        sales.columns = ["customer_id", "product_id", "sales"]

        # ------------------ LOAD ------------------
        conn = sqlite3.connect("db/warehouse.db")

        customers.to_sql("customers", conn, if_exists="replace", index=False)
        products.to_sql("products", conn, if_exists="replace", index=False)
        sales.to_sql("sales", conn, if_exists="replace", index=False)

        st.success("✅ Data Warehouse Created Successfully!")

        # ------------------ DISPLAY ------------------
        st.subheader("👥 Customers Table")
        st.dataframe(customers)

        st.subheader("📦 Products Table")
        st.dataframe(products)

        st.subheader("💰 Sales Table")
        st.dataframe(sales)

        # ------------------ ANALYSIS ------------------
        query = """
        SELECT p.product_name, SUM(s.sales) as total_sales
        FROM sales s
        JOIN products p ON s.product_id = p.product_id
        GROUP BY p.product_name
        ORDER BY total_sales DESC
        LIMIT 5;
        """

        result = pd.read_sql(query, conn)

        st.subheader("📊 Top 5 Products")
        st.bar_chart(result.set_index("product_name"))

        conn.close()

else:
    st.info("👆 Upload a CSV file to begin")