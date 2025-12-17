import pandas as pd
import sqlite3
import os

# --- PATH CONFIGURATION  ---
# Gets the directory where this script is located
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Define paths for the CSV file and the Database
csv_path = os.path.join(base_dir, 'data', 'crop_yield.csv')
db_path = os.path.join(base_dir, 'database', 'agri_project.db')

def etl_process():
    print("🔄 Starting ETL process...")

    # 1. EXTRACT
    if not os.path.exists(csv_path):
        print(f"❌ Error: File not found at {csv_path}")
        return
    
    try:
        df = pd.read_csv(csv_path)
        print(f"✅ Data Loaded: {len(df)} rows found.")
        
        # Basic Cleaning: Standardize column names (lowercase, no spaces)
        # This makes writing SQL queries much easier later.
        df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
        
        # Renaming specific columns
        df.rename(columns={'unnamed:_0': 'id', 'hg/ha_yield': 'yield', 'area': 'country'}, inplace=True)
        
        print(f"📋 Detected Columns: {list(df.columns)}")
        
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return

    # 2. LOAD
    try:
        conn = sqlite3.connect(db_path)
        
        # 'if_exists="replace"' recreates the table every time you run the script
        df.to_sql('yield_data', conn, if_exists='replace', index=False)
        
        conn.close()
        print(f"🚀 Success! Database created at: {db_path}")
        print("Table created: 'yield_data'")
        
    except Exception as e:
        print(f"❌ Error saving to SQL: {e}")

if __name__ == "__main__":
    etl_process()