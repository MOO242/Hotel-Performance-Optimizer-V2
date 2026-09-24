#!/usr/bin/env python
# coding: utf-8

# ## 📊 Comprehensive EDA Checklist — Python & Pandas

# ### 1- Setup — imports (run once)

# In[47]:


import os
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
from sqlalchemy import create_engine


# ### 2- Upload data to PostgreSQL

# In[48]:


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
    table_name = Path(path).stem

    df.to_sql(
        con=engine,
        chunksize=5000,
        index=False,
        if_exists="replace",
        name=table_name,
    )


# Load all dimension and fact tables into db
data_files = [
    "dim_customers.csv",
    "dim_date.csv",
    "dim_hotels.csv",
    "dim_rooms.csv",
    "fact_reservations.csv",
    "fact_room_inventory.csv",
]


for file in data_files:
    file_path = os.path.join(r"D:\Hotel-Performance-Optimizer-V2\notebook", file)
    data_load(file_path)

# Read tables from db


def read_table(table_name):
    return pd.read_sql(f"SELECT * FROM {table_name}", engine)


# ### 3 - Merging Tables

# In[49]:


join_plan = [
    ("dim_customers", "customer_id", "customer_id"),
    ("dim_date", "booking_date_key", "date_key"),
    ("dim_rooms", "room_id", "room_id"),
]

fact_reservations_enrichment = read_table("fact_reservations")


for table_name, table_left_key, table_right_key in join_plan:
    before = len(fact_reservations_enrichment)
    dim_df = read_table(table_name)

    fact_reservations_enrichment = pd.merge(
        fact_reservations_enrichment,
        dim_df,
        how="inner",
        left_on=table_left_key,
        right_on=table_right_key,
    )

    after = len(fact_reservations_enrichment)
    print(f"{table_name}: {before} -> {after} rows.")


# In[50]:


join_plan = [
    ("dim_date", "date_key", "date_key"),
    ("dim_hotels", "property_id", "property_id"),
]

fact_room_inventory_enrichment = read_table("fact_room_inventory")

for table_name, left_key, right_key in join_plan:
    before = len(fact_room_inventory_enrichment)
    dim_df = read_table(table_name)
    fact_room_inventory_enrichment = pd.merge(
        fact_room_inventory_enrichment,
        dim_df,
        how="inner",
        left_on=left_key,
        right_on=right_key,
    )
    after = len(fact_room_inventory_enrichment)
    print(f"{table_name}: {before} -> {after} rows")


# ### 4 -  LOAD & INSPECT
# 

# In[51]:


# Tables after joins

fact_room_inventory_enrichment.head()


# In[52]:


fact_reservations_enrichment.head()


# In[53]:


# ---------- STEP 1: First Look at the Data ----------

# Data Overview for first table fact_reservations_enrichment

# def data_overview(path):

# print(path.shape)
# print(path.dtypes)
# path.head(5)
# print(path.describe())
# print(path.select_dtypes(include=["object", "category"]))
# print(fact_reservations_enrichment.nunique())
# fact_reservations_enrichment.info(memory_usage='deep')


# data_overview(fact_reservations_enrichment)


# In[54]:


# 2. Data Types & Structure

# I found that the check_in and check_our data type is int64 so I will change it to datetime64 for analysis

fact_reservations_enrichment["check_in_date_key"] = pd.to_datetime(
    fact_reservations_enrichment["check_in_date_key"].astype("str")
)
fact_reservations_enrichment["checkout_date_key"] = pd.to_datetime(
    fact_reservations_enrichment["checkout_date_key"].astype("str")
)
fact_reservations_enrichment["date"] = pd.to_datetime(
    fact_reservations_enrichment["date"].astype("str")
)
fact_reservations_enrichment.dtypes


# In[55]:


# I found that several columns had an object dtype, which was taking up too much memory.
# After converting them to category, memory usage dropped from 275 MB to 110 MB.

cols_to_convert = fact_reservations_enrichment[
    [
        "month_name",
        "customer_segment",
        "nationality",
        "country",
        "property_id",
        "room_id",
        "booking_channel",
        "market_segment",
        "booking_status",
        "room_class",
        "room_category",
    ]
]
cols_to_convert = cols_to_convert.astype("category")
fact_reservations_enrichment.info(memory_usage="deep")


# In[56]:


fact_reservations_enrichment


# In[57]:


# ---------- STEP 2: DATA CLEANING ----------

# Missing Values

fact_reservations_enrichment.isnull().sum()

# Finding : I found the loyalty_tier has 199266, approx 40% of the data is missing. I Will deal with in part 3 predictive phase when creating a Model.

(fact_reservations_enrichment.isnull().mean() * 100).round(2)


# Duplicates

(fact_reservations_enrichment.duplicated().mean() * 100).round(2)

(fact_reservations_enrichment.duplicated(subset=["booking_id"]).mean() * 100).round(2)


# ### 5- Univariate Analysis (one column at a time)

# In[58]:


fact_reservations_enrichment["booking_status"].value_counts(dropna=False)


# In[59]:


# ---------- STEP 3: Univariate Analysis (one column at a time) ----------

# Part 1 : Room Revenue per room pool

fact_reservations_enrichment["booking_status"].value_counts()

data_com = fact_reservations_enrichment[
    ~fact_reservations_enrichment["booking_status"].isin(["Cancelled", "No Show"])
    & fact_reservations_enrichment["room_id"].isin(["RT1"])
].copy()

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

sns.histplot(data=(data_com["room_revenue"]), bins=20, kde=True, ax=axes[0])

axes[0].set_title("Distribution")

sns.boxplot(x=(data_com["room_revenue"]), ax=axes[1])

axes[1].set_title("Boxplot")
plt.tight_layout()
plt.show()

print(f"Mean: {data_com['room_revenue'].mean():.2f}")
print(f"Median: {data_com['room_revenue'].median():.2f}")
print(f"Skew: {data_com['room_revenue'].skew():.2f}")
print(f"Standard  Division: {data_com['room_revenue'].std():.2f}")
print(f"Kurtosis: {(data_com['room_revenue']).kurt():.2f}")


# In[60]:


# Part 2 : Outlier Detection

Q1 = data_com["room_revenue"].quantile(0.25)
Q3 = data_com["room_revenue"].quantile(0.75)
IQR = Q3 - Q1

lower, upper = Q1 - (1.5 * IQR), Q3 + (1.5 * IQR)

outliers = data_com[
    (data_com["room_revenue"] < lower) | (data_com["room_revenue"] > upper)
]
print(f"Outliers: {len(outliers):,} ({len(outliers)/len(data_com)*100:.2f}%)")
print(f"Fences → lower: {lower:.2f}, upper: {upper:.2f}")


# In[62]:


outliers


# In[69]:


# Part 3 — Outlier Decision

outliers.assign(
    adr = lambda d: d["room_revenue"] / d["length_of_stay"]
)[["room_revenue", "length_of_stay", "adr"]].describe()

# Inspect the biggest ones
# outliers.nlargest(10, "room_revenue")[["room_revenue", "length_of_stay"]]


# In[64]:


outliers.nlargest(10, "room_revenue")[["room_revenue", "length_of_stay"]]


# In[72]:


outliers


# In[77]:


long_stay = data_com["length_of_stay"] >= 4

data_com.groupby(long_stay).agg(
rows = ("room_revenue", "size"),
revenue = ("room_revenue", "sum"),
avg_los = ("length_of_stay", "mean"),
)

