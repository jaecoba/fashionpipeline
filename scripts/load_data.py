import os
from sqlalchemy import create_engine
from transform_data import transform_data
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

engine = create_engine(DATABASE_URL)

def load_data(data, table_name='fashion_trends'):
    try:
        data.to_sql(table_name, engine, if_exists='append', index=True)
    except Exception as e:
        print(f"Error loading data to {table_name}: {e}")

data = pd.read_csv('../data/trend_data.csv')
transformed_data = transform_data(data)
load_data(transformed_data)