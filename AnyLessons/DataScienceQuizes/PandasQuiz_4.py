import pandas as pd

df = pd.read_csv("https://www.sololearn.com/uploads/ca-covid.csv")

df.drop('state', axis=1, inplace=True)
df['date'] = pd.to_datetime(df['date'], format="%d.%m.%y")
df['month'] = df['date'].dt.month_name()
df.set_index('date', inplace=True)

month = df[df.month == input()]
max_day = month.cases.max()
# # min_day = month.cases.min()
# # max_deaths = month.deaths.max()
print(month[month.cases == max_day])
# # print(month[month.cases == min_day])
# # print(month[month.deaths == max_deaths])


#  А эта штука выведет только значение без заголовков
# month = input()
# print(
#     df[(df['month'] == month)]['cases'].max()
# )
