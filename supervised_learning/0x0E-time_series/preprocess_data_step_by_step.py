#!/usr/bin/env python3
"""
Preprocess the Coinbase dataset
"""
import matplotlib.pyplot as plt
import pandas as pd

# Read the data
file_path = './bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv'
df_bitstamp = pd.read_csv(file_path)
file_path = './coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv'
df_coinbase = pd.read_csv(file_path)
print("df_bitstamp:\n", df_bitstamp)
print("df_coinbase:\n", df_coinbase)

# Timestamp to date
df_bitstamp['Timestamp'] = pd.to_datetime(df_bitstamp['Timestamp'], unit='s')
df_coinbase['Timestamp'] = pd.to_datetime(df_coinbase['Timestamp'], unit='s')
print("\ndf_bitstamp after convert timestanp to date:\n", df_bitstamp)
print("df_coinbase after convert timestanp to date:\n", df_coinbase)

# Count NaN values
nb_nan_coinbase = df_coinbase.isna().sum()
nb_nan_bitstamp = df_bitstamp.isna().sum()
print("number of NaN:\n", nb_nan_coinbase, "\n")
print("number of NaN:\n", nb_nan_bitstamp, "\n")

# Replace coinbase Nan values by bitstamp dataframe values
df_bitstamp = df_bitstamp.set_index('Timestamp')
df_coinbase = df_coinbase.set_index('Timestamp')
df_coinbase = df_coinbase.fillna(df_bitstamp)
print("df_coinbase after replace NaN:\n", df_coinbase)

# Recount NaN values
nb_nan_coinbase = df_coinbase.isna().sum()
print("number of NaN:\n", nb_nan_coinbase, "\n")

# Replace coinbase Nan values by previous ones
df_coinbase.ffill(inplace=True)

# Recount NaN values
nb_nan_coinbase = df_coinbase.isna().sum()
print("no more NaN:\n", nb_nan_coinbase, "\n")

# check types
print("\ntypes:")
print(df_coinbase.dtypes)

# number of unique values
print("\nnumber of unique values:")
print(df_coinbase.nunique())

# Drop column
colums_to_dropped = ['Open', 'High', 'Low', 'Volume_(BTC)']
df_coinbase = df_coinbase.drop(colums_to_dropped, axis=1)
print("\ndf_coinbase after dropping colums:\n", df_coinbase)

# Describe data
print("data description:\n", df_coinbase.describe())

# export the preprocessed data
df_coinbase.to_csv('./coinbase_preprocessed.csv', index=False)
