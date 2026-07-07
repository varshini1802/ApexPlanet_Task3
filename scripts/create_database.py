import pandas as pd
from sqlalchemy import create_engine
import os

# Get the project root folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# CSV file path
csv_path = os.path.join(BASE_DIR, "data", "superstore_cleaned.csv")

# SQLite database path
db_path = os.path.join(BASE_DIR, "data", "sales_data.db")

# Read CSV
df = pd.read_csv(csv_path)

# Create SQLite database
engine = create_engine(f"sqlite:///{db_path}")

# Import data into SQLite
df.to_sql("superstore_cleaned", con=engine, if_exists="replace", index=False)

print("✅ Database created successfully!")
print(f"Rows Imported : {len(df)}")
print(f"Columns : {len(df.columns)}")
print(f"Database Saved At : {db_path}")