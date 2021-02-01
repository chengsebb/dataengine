import numpy as np
import pandas as pd
df = pd.read_excel('list.xlsx', sheet_name='Sheet2')
print(df)
print(df.describe())
df['总成绩'] = df.sum(axis=1)
print(df.sort_values(by='总成绩').reset_index(drop=True))
