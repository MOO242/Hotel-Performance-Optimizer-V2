import os
from os import path
from dotenv import load_dotenv
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

load_dotenv()

base_dir = Path(__file__).parent

""" SQL Connection"""

DB_SERVER_HOST = os.getenv("POSTGRES_HOST")
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_LOCAL_PORT = os.getenv("POSTGRES_PORT")


engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER_HOST}:{DB_LOCAL_PORT}/{DB_NAME}"
)


file_path = base_dir / "notebook" / "dim_customers.csv"

df = pd.read_csv(file_path)


df.to_sql(
    name="dim_customers.csv",
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=5000,
)
