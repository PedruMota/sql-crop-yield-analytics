import sqlite3
import os
import pandas as pd

# 1. Database Connection
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(base_dir, 'database', 'agri_project.db')
conn = sqlite3.connect(db_path)

def run_query(query_text, title="Query Result"):
    print(f"\n--- {title} ---")
    try:
        # Pandas reads SQL and returns a DataFrame
        df = pd.read_sql_query(query_text, conn)
        print(df)
        return df
    except Exception as e:
        print(f"❌ SQL Error: {e}")
        return None

# ==========================================
# 🧠 SQL ANALYSIS
# ==========================================

# Query 1: Sanity Check (View raw data)
query_1 = """
SELECT country, item, year, yield 
FROM yield_data 
LIMIT 5;
"""

# Query 2: Top 5 Crops by Average Yield (Performance)
# Quais culturas têm a maior produtividade média histórica?
query_2 = """
SELECT item, AVG(yield) as avg_yield_hg_ha
FROM yield_data
GROUP BY item
ORDER BY avg_yield_hg_ha DESC
LIMIT 5;
"""

# Query 3: Climate Impact (Rain vs Yield) for a specific crop
# Vamos ver a média de chuva e produtividade por ano (exemplo geral)
query_3 = """
SELECT 
    year, 
    AVG(average_rain_fall_mm_per_year) as avg_rain, 
    AVG(yield) as avg_yield
FROM yield_data
GROUP BY year
ORDER BY year ASC
LIMIT 10;
"""

# Execution
run_query(query_1, "1. Data Preview")
run_query(query_2, "2. Top 5 Crops (Highest Yield)")
run_query(query_3, "3. Year vs Rain vs Yield")

conn.close()