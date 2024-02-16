#!/usr/bin/env python3
"""
Preprocess the Coinbase dataset
"""
import pandas as pd

# Read the data
file_path = './bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv'
df_bitstamp = pd.read_csv(file_path)
file_path = './coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv'
df_coinbase = pd.read_csv(file_path)

# Timestamp to date
df_bitstamp['Timestamp'] = pd.to_datetime(df_bitstamp['Timestamp'], unit='s')
df_coinbase['Timestamp'] = pd.to_datetime(df_coinbase['Timestamp'], unit='s')

# Replace coinbase Nan values by bitstamp dataframe values
df_bitstamp = df_bitstamp.set_index('Timestamp')
df_coinbase = df_coinbase.set_index('Timestamp')
df_coinbase = df_coinbase.fillna(df_bitstamp)
df_coinbase.ffill(inplace=True)

# Drop columns
colums_to_dropped = ['Open', 'High', 'Low', 'Volume_(BTC)']
df_coinbase = df_coinbase.drop(colums_to_dropped, axis=1)

# export the preprocessed data
df_coinbase.to_csv('./coinbase_preprocessed.csv', index=False)
