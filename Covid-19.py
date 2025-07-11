import pandas as pd
df = pd.read_csv("C:/Users/Dell/Desktop/Mine/DATASET/Covid-19/Covid-data.csv")
print(df.head())
df = df[['location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'people_vaccinated', 'continent']]
df = df.dropna(subset=['location', 'date'])
df.to_csv("C:/Users/Dell/Desktop/Mine/DATASET/Covid-19/Covid 19.csv", index=False)