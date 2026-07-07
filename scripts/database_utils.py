import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///data/sales_data.db")

def run_query(query):
    return pd.read_sql(query, engine)