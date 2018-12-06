import pandas as pd

df = pd.read_csv("C:\\Users\\Sun of sadi\\Desktop\\Data\\nyc_weather.csv")
print(df.head())
print(df['Temperature'].max())
print(df['EST'][df['Events'] == 'Rain'])
df.fillna(0,inplace=True)
print(df['WindSpeedMPH'].mean())
