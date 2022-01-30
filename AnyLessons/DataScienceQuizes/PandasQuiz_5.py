import pandas as pd

df = pd.read_csv("https://www.sololearn.com/uploads/ca-covid.csv")

df.drop('state', axis=1, inplace=True)
df.set_index('date', inplace=True)

df['ratio'] = df['deaths'] / df['cases']  # создание нового столбца ratio и его значений

print(
    df[
        (
            df['ratio'] == df['ratio'].max()  # так будет выведен весь датафрейм по максимальному значению ratio
        )
    ]
)
