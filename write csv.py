import pandas as pd

wether = pd.read_csv("C:\\Users\\Sun of sadi\\Desktop\\Data\\weather_data.csv")
print(wether)

stock = pd.read_csv("C:\\Users\\Sun of sadi\\Desktop\\Data\\stock_data.csv")
print(stock)

#write two excel file in one excel create stock_weather
with pd.ExcelWriter("stock_weathe.xlsx")as writer:
    wether.to_excel(writer,sheet_name="weather")
    stock.to_excel(writer,sheet_name="stock")