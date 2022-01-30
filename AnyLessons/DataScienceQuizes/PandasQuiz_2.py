import pandas as pd

df = pd.read_csv("https://www.sololearn.com/uploads/ca-covid.csv")
df.set_index('date', inplace=True)  # "date" - один из столбцов в датафрейме df, делаем его индексом.
df.drop('state', axis=1, inplace=True)
print(df.loc['31.12.20'])
