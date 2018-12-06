import pandas as pd

# header missing then use header None and set names,header false means skip header
# df = pd.read_csv("C:\\Users\\Sun of sadi\\Desktop\\Data\\stock_data.csv",header=None, names=["ticket","eps","Revenue","price","people"])
# print(df)

#limit print result then use nrows
# df = pd.read_csv("C:\\Users\\Sun of sadi\\Desktop\\Data\\stock_data.csv",nrows=3)
# print(df)

#cleaning messy data fill up NAN.
# df = pd.read_csv("C:\\Users\\Sun of sadi\\Desktop\\Data\\stock_data.csv", na_values=["not available","n.a.","-1"])
# print(df)

#create dictionary then cleaning messy data fill up NAN
df = pd.read_csv("C:\\Users\\Sun of sadi\\Desktop\\Data\\stock_data.csv", na_values={
    'eps': ["not available","n.a."],
    'revenue': ["not available","n.a.","-1"],
    'people': ["not available","n.a.","-1"]

})

print(df)


#create new csv two columns df
df.to_csv("new_stock.csv",index=False,columns=["tickers","eps"])
df1 = pd.read_csv('new_stock.csv',)
print(df1.columns)
print(df1)

