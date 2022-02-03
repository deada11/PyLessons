import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://www.sololearn.com/uploads/ca-covid.csv")
df.drop('state', axis=1, inplace=True)
df['date'] = pd.to_datetime(df['date'], format="%d.%m.%y")
df['month'] = df['date'].dt.month
df.set_index('date', inplace=True)

# df[df['month']==12]['cases'].plot()
# (df[df['month']==12])[['cases', 'deaths']].plot()
# (df.groupby('month')['cases'].sum()).plot(kind="bar")

# df = (df.groupby('month')[['cases', 'deaths']].sum()).plot(kind="bar", stacked=True)

# df[df["month"]==6]["cases"].plot(kind="box")

df[df["month"]==6]["cases"].plot(kind="hist")

# df[df["month"]==6][["cases", "deaths"]].plot(kind="area", stacked=False)

# df[df["month"] == 6][["cases", "deaths"]].plot(kind="scatter", x='cases', y='deaths')

# df.groupby('month')['cases'].sum().plot(kind="pie")

# df[['cases', 'deaths']].plot(kind="line", legend=True, stacked=False, color=['#000000', '#AAAFFF'])
# plt.xlabel('Days in June')
# plt.ylabel('Number')
# plt.suptitle("COVID-19 in June")

plt.savefig('plot.png')
