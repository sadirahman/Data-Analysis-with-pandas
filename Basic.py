import pandas as pd

df = pd.read_csv("C:\\Users\\Sun of sadi\\Desktop\\Data\\weather_data.csv")
print(df)
print(df.shape)

row,column = df.shape

print(row)
print(column)
print(df.day)
print(df[['day','event','temperature']])
print(df)

#maximum temperature score
max_tem = df['temperature'].max()
print("maximum temperature:",max_tem)

#minimum temperature
min_tem = df['temperature'].min()
print("minimum temperature :",min_tem)

#avarage temperature
avg_tem = df['temperature'].mean()
print("avarage temperature:",avg_tem)

#Standerd temperature
std_tem = df['temperature'].std()
print("Standerd temperature:",std_tem)

#describe csv
describe_csv = df.describe()
print(describe_csv)

#maximum tempurature rows
max_tem_row = df[df['temperature'] == df['temperature'].max()]
print(max_tem_row)

#spacific attributes
max_tem_row = df[['day','temperature',]][df['temperature'] == df['temperature'].max()]
print(max_tem_row)
