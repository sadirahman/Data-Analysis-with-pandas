import pandas as pd

# header missing then use header None and set names,header false means skip header
# df = pd.read_csv("C:\\Users\\Sun of sadi\\Desktop\\Data\\stock_data.xlsx",header=None, names=["ticket","eps","Revenue","price","people"])
# print(df)

#limit print result then use nrows
# df = pd.read_csv("C:\\Users\\Sun of sadi\\Desktop\\Data\\stock_data.xlsx",nrows=3)
# print(df)

#cleaning messy data fill up NAN.
# df = pd.read_csv("C:\\Users\\Sun of sadi\\Desktop\\Data\\stock_data.xlsx", na_values=["not available","n.a.","-1"])
# print(df)


def convert_people (cell):
    if cell =="n.a.":
        return "sadi"
    return cell
def convert_eps(cell):
    if cell=="not available":
        return None
    return cell
def convert_revenue(cell):
    if cell == -1:
        return None
    return cell


#create dictionary then cleaning messy data fill up NAN
df = pd.read_excel("C:\\Users\\Sun of sadi\\Desktop\\Data\\stock_data.xlsx","Sheet1", converters={
    'eps' : convert_eps,
    'people': convert_people,
    'revenue':convert_revenue

})

print(df)


# #create new csv two columns
df.to_excel("new_stock.xlsx",sheet_name="stocks",index=False,columns=["tickers","eps"],startrow=1,startcol=2)
df1 = pd.read_excel('new_stock.xlsx')
print(df1)


wether = pd.read_csv("C:\\Users\\Sun of sadi\\Desktop\\Data\\weather_data.csv")
print(wether)

stock = pd.read_csv("C:\\Users\\Sun of sadi\\Desktop\\Data\\stock_data.csv")
print(stock)

#write two excel file in one excel create stock_weather
with pd.ExcelWriter("stock_weathe.xlsx")as writer:
    wether.to_excel(writer,sheet_name="weather")
    stock.to_excel(writer,sheet_name="stock")


