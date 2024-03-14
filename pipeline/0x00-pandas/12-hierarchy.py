#!/usr/bin/env python3

import pandas as pd
from_file = __import__('2-from_file').from_file

df1 = from_file(
    'data/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')
df2 = from_file(
    'data/bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv', ',')

df1 = df1.loc[(df1['Timestamp'] >= 1417411980) &
              (df1['Timestamp'] <= 1417417980)].set_index('Timestamp')
df2 = df2.loc[(df2['Timestamp'] >= 1417411980) &
              (df2['Timestamp'] <= 1417417980)].set_index('Timestamp')

df = pd.concat([df2, df1], keys=['bitstamp', 'coinbase'])
df = df.swaplevel(0, 1, axis=0).sort_index()

print(df)
