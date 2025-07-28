import pandas as pd
from sqlalchemy import create_engine, text
import mysql.connector

# === CONFIGURATION ===
DB_USER = "root"
DB_PASSWORD = "your_password"  # Change this
DB_HOST = "localhost"
DB_NAME = "stock_dashboard_db"
TABLE_NAME = "stocks"
CSV_FILE = "stock_market_june2025.csv"

# === STEP 1: Read and clean the CSV ===
df = pd.read_csv(CSV_FILE)

# Parse dates and drop rows with invalid dates
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])

# Optional: Replace NaNs with defaults
df.fillna({'Ticker': 'N/A', 'Sector': 'Unknown'}, inplace=True)
df.fillna(0, inplace=True)

# === STEP 2: Connect to MySQL and create table ===
engine = create_engine(f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")

with engine.connect() as conn:
    # Drop existing table (optional)
    conn.execute(text(f"DROP TABLE IF EXISTS {TABLE_NAME}"))

    # Create table
    create_table_query = f"""
    CREATE TABLE {TABLE_NAME} (
        Ticker VARCHAR(20),
        Date DATE,
        `Open Price` FLOAT,
        `Close Price` FLOAT,
        High FLOAT,
        Low FLOAT,
        Volume BIGINT,
        Sector VARCHAR(100),
        `Market Cap` BIGINT,
        PRIMARY KEY (Ticker, Date)
    );
    """
    conn.execute(text(create_table_query))
    print(f"✅ Table `{TABLE_NAME}` created in `{DB_NAME}` database.")

# === STEP 3: Insert the data ===
df.to_sql(TABLE_NAME, con=engine, if_exists="append", index=False)
print("✅ Data successfully inserted into MySQL!")
