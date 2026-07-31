#!/usr/bin/env python

# ### Exploratory Data Analysis

# ### Upload data to PostgreSQL

# In[24]:


import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import seaborn as sns
from dotenv import load_dotenv
from sqlalchemy import create_engine

# In[25]:


load_dotenv()

DB_SERVER_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")

engine = create_engine(
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_SERVER_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)


def data_load(path):

    df = pd.read_csv(path)

    df.to_sql(
        con=engine,
        chunksize=5000,
        index=False,
        if_exists="replace",
        name=path,
    )


data_load(r"D:\Hotel-Performance-Optimizer-V2\notebook\dim_customers.csv")


def read_table(path):

    df = pd.read_sql(f"SELECT * FROM {path}", engine)
    return df


# ## Merging Tables

# In[26]:


join_plan = [
    ("dim_customers", "customer_id", "customer_id"),
    ("dim_date", "check_in_date_key", "date_key"),
    ("dim_hotels", "property_id", "property_id"),
    ("dim_rooms", "room_id", "room_id"),
]

reservations_enriched = read_table("fact_reservations")

for table_name, left_key, right_key in join_plan:
    before = len(reservations_enriched)
    dim_df = read_table(table_name)
    reservations_enriched = pd.merge(
        reservations_enriched, dim_df, how="inner", left_on=left_key, right_on=right_key
    )
    after = len(reservations_enriched)
    print(f"{table_name}: {before} -> {after} rows")


# In[27]:


join_plan = [
    ("dim_date", "date_key", "date_key"),
    ("dim_hotels", "property_id", "property_id"),
]

property_daily = read_table("fact_room_inventory")

for table_name, left_key, right_key in join_plan:
    before = len(property_daily)
    dim_df = read_table(table_name)
    property_daily = pd.merge(
        property_daily, dim_df, how="inner", left_on=left_key, right_on=right_key
    )
    after = len(property_daily)
    print(f"{table_name}: {before} -> {after} rows")


# # DATA OVERVIEW
#

# In[28]:


# ---------- STEP 1: DATA OVERVIEW ----------


def data_overview(path):

    print(path.shape)
    print(path.dtypes)
    print(path.head())
    print(path.describe(include=["object", "category"]))


data_overview(reservations_enriched)


# In[29]:


# ---------- STEP 2: DATA CLEANING ----------


def data_cleaning(path):
    print(path.isnull().sum())
    print(path.isnull().sum() / len(path) * 100)


# data_cleaning(reservations_enriched)

# Finding : I found the loyalty_tier has 199266, approx 40% of the data is missing. I Will deal with in part 3 predictive phase when creating a Model.


def dupes(path):

    print(path.duplicated().sum())


dupes(reservations_enriched)
