import pandas as pd
from functions import *

# import csv from path
df = pd.read_csv('gastos.csv')

# convert datetime objects
df['datetime'] = pd.to_datetime(df['datetime'])

# sort dataframe
df = df.sort_values(by='datetime', ascending=False)

# create new columns
df = df.assign(
    quarter = df['datetime'].dt.to_period('Q').astype(str),
    period = df['datetime'].dt.to_period('M').astype(str),
    date = (df['datetime']).dt.to_period('D').astype(str),
    month = df['datetime'].dt.month_name(),
    week = df['datetime'].apply(get_week),
    trip = df['detail'].apply(get_trip),
    person = df['detail'].apply(get_person)
)