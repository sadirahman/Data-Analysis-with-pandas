import pandas as pd

#CSV file
df_csv = pd.read_csv("C:\\Users\\Sun of sadi\\Desktop\\Data\\weather_cr.csv")
print(df_csv)

#Excel file
df_xlsx = pd.read_excel("C:\\Users\\Sun of sadi\\Desktop\\Data\\weather_data.xlsx","Sheet1")
print(df_xlsx)

#create dictionary
weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'windspeed': [6,7,2],
    'event': ['Rain', 'Sunny', 'Snow']
}
df_Dic = pd.DataFrame(weather_data)
print(df_Dic)


weather_data = [
    ('1/1/2017',32,6,'Rain'),
    ('1/2/2017',35,7,'Sunny'),
    ('1/3/2017',28,2,'Snow')
]
df = pd.DataFrame(data=weather_data, columns=['day','temperature','windspeed','event'])
print(df)

weather_data = [
    {'day': '1/1/2017', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
    {'day': '1/2/2017', 'temperature': 35, 'windspeed': 7, 'event': 'Sunny'},
    {'day': '1/3/2017', 'temperature': 28, 'windspeed': 2, 'event': 'Snow'},

]
df = pd.DataFrame(data=weather_data, columns=['day', 'temperature', 'windspeed', 'event'])
print(df)
print(df.columns)

