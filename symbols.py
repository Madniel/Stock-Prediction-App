import pandas as pd

df = pd.read_csv('symbols.csv')
df = df.loc[:,['Symbol', 'Name']]
df = df.set_index('Name')
df.to_csv('companies.csv')
print(df)