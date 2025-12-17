# SQL Agro Pipeline 🚜 🌽

![SQL](https://img.shields.io/badge/Skill-SQL-orange)
![Python](https://img.shields.io/badge/Code-Python%20%7C%20Pandas-blue)
![Database](https://img.shields.io/badge/Database-SQLite-lightgrey)

## 📋 Project Overview
This project demonstrates an end-to-end **Data Engineering** pipeline applied to the Agriculture sector. 

The goal was to transform raw, unstructured data (CSV) into a high-performance **Star Schema Data Warehouse** using Python for ingestion and **SQL** for data modeling and analysis. The project focuses on analyzing global crop yield trends and Year-Over-Year (YoY) growth using Window Functions.

## ⚙️ Architecture & Technologies
* **Ingestion (ETL):** Python (`Pandas`) to clean and load raw CSV data into a staging area.
* **Database:** SQLite (embedded relational database).
* **Data Modeling:** Transformation of flat tables into a **Star Schema** (Fact & Dimensions) using SQL DDL.
* **Analysis:** Complex queries using **Window Functions** (`LAG`, `OVER`), **CTEs**, and **Views** for anomaly detection.

## 🗂️ Data Modeling (Star Schema)
To ensure data integrity and query performance, the database was normalized from a single flat table into a Relational Schema:

* **Fact Table:** `fact_crop_yields` (Contains metrics: Yield, Rainfall, Temperature, Pesticides).
* **Dimension Tables:** `dim_crops`, `dim_countries`.

## 🧠 Key SQL Skills Demonstrated
The core of this project is the `notebooks/sql_data_modeling.ipynb` file, which covers:

1.  **Normalization:** Converting raw text columns into normalized Dimension tables.
2.  **Window Functions:** Using `LAG()` to calculate **Year-over-Year Growth %**:
    ```sql
    LAG(current_yield) OVER (PARTITION BY crop_name ORDER BY year)
    ```
3.  **Data Quality Views:** Creating a persistent SQL View (`view_data_anomalies`) to automatically flag data outliers (e.g., Temperature > 40°C).

## 🚀 How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/PedruMota/Advanced-SQL-Agro-Pipeline.git](https://github.com/PedruMota/sql-crop-yield-analytics.git)
    cd Advanced-SQL-Agro-Pipeline
    ```

2.  **Set up the environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Run the ETL Pipeline:**
    ```bash
    python src/01_ingest_data.py
    ```

4.  **Explore the Analysis:**
    Open `notebooks/sql_data_modeling.ipynb` in VS Code or Jupyter Lab to see the step-by-step SQL transformation.

## 📊 Sample Results

| Year | Crop  | Yield (hg/ha) | Growth %   |
|------|-------|---------------|------------|
| 1993 | Maize | 28,997        | 📈 +3.70%  |
| 1994 | Maize | 28,344        | 📉 -2.25%  |
| 1996 | Maize | 30,763        | 📈 +5.35%  |

---
*Author: Pedro Mota*
*Dataset Source: [Kaggle Crop Yield Prediction](https://www.kaggle.com/datasets/patelris/crop-yield-prediction-dataset)*
...
