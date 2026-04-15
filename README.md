# 📊 Mini Data Warehouse & Sales ETL Pipeline

## 🚀 Project Overview

This project demonstrates an end-to-end **Data Engineering pipeline** where raw sales data is processed, transformed, and stored into a structured **data warehouse**. The project also includes an interactive **Streamlit dashboard** that allows users to upload their own datasets and generate insights in real time.

---

## 🎯 Key Features

* 📥 Upload custom CSV datasets
* 🔄 ETL Pipeline (Extract, Transform, Load)
* 🧹 Data cleaning (handling nulls, duplicates, formatting)
* 🏗️ Data warehouse creation (Star Schema)
* 🗄️ SQLite database integration
* 📊 Interactive dashboard using Streamlit
* ⚡ Real-time data processing and visualization

---

## 🛠️ Tech Stack

* **Python**
* **Pandas**
* **SQL (SQLite)**
* **Streamlit**

---

## 📂 Project Structure

```
mini_data_warehouse/
│
├── data/              # Input datasets
├── src/               # ETL & warehouse scripts
├── db/                # SQLite database
├── app/               # Streamlit app
│   └── app.py
└── README.md
```

---

## ⚙️ How It Works

### 1️⃣ Extract

* Load raw CSV data using Pandas

### 2️⃣ Transform

* Clean data (remove nulls, duplicates)
* Standardize column names
* Create derived columns
* Generate IDs for entities

### 3️⃣ Load

* Store processed data into SQLite database
* Create:

  * **Fact Table:** Sales
  * **Dimension Tables:** Customers, Products

### 4️⃣ Analyze

* Perform SQL queries
* Generate insights (top products, sales trends)

### 5️⃣ Visualize

* Interactive dashboard using Streamlit

---

## ▶️ Run Locally

### Step 1: Install dependencies

```
python3 -m pip install pandas streamlit
```

### Step 2: Run ETL / Warehouse script

```
python3 src/warehouse.py
```

### Step 3: Launch Streamlit app

```
python3 -m streamlit run app/app.py
```

---

## 🌐 Streamlit App Features

* Upload your own dataset
* Map columns dynamically
* Automatically build data warehouse
* View structured tables
* Visualize top-performing products

---

## 📊 Example Insights

* Top-selling products
* Category-wise revenue
* Customer purchase patterns

---

## 💡 Use Cases

* Retail sales analysis
* Business intelligence dashboards
* Data engineering learning project
* Real-time dataset exploration

---

## 🎤 What I Learned

* Building ETL pipelines using Python
* Data cleaning and transformation techniques
* Designing star schema (data warehouse)
* Writing SQL queries for analysis
* Creating interactive dashboards with Streamlit

---

## 🚀 Future Improvements

* Add filters (date/category)
* Advanced visualizations
* Cloud deployment
* Real-time data ingestion (API integration)

---
Live Demo:https://38katsanskriti.streamlit.app/

## 👩‍💻 Author

**Sanskriti**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!

