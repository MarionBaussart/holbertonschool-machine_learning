#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('data/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

df = df.drop(columns=['Weighted_Price'])
df = df.rename(columns={'Timestamp': 'Date'})
df['Date'] = pd.to_datetime(df['Date'], unit='s')

date_mask = (df['Date'] >= '2017-01-01')
df = df.loc[date_mask]

df = df.set_index('Date')
df['Close'] = df['Close'].ffill()
df['High'] = df['High'].fillna(df['Close'])
df['Low'] = df['Low'].fillna(df['Close'])
df['Open'] = df['Open'].fillna(df['Close'])
df[['Volume_(BTC)', 'Volume_(Currency)']] = df[['Volume_(BTC)',
                                                'Volume_(Currency)']].fillna(0)

df = df.groupby(pd.Grouper(freq='d')).agg({'High': 'max',
                                           'Low': 'min',
                                           'Open': 'mean',
                                           'Close': 'mean',
                                           'Volume_(BTC)': 'sum',
                                           'Volume_(Currency)': 'sum'})

plot = df.plot()
plt.show()
