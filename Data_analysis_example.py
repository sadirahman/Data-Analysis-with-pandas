import pandas as pd

def Number_of_line(cell):
    if cell =="None":
        return 'NaN'
    return cell

df = pd.read_excel("C:\\Users\\Sun of sadi\\PycharmProjects\\Pandas\Data\\Demo.xlsx", "Sheet1", converters={
      'Number  of line': Number_of_line
})
print(df)
df.to_excel('New_Data.xlsx',sheet_name='Demo')
print(df)

print("show Our result:")


Group = df.groupby('Name')
for Name,name_df in Group:
    print(Name)
    print(name_df)
    print(name_df.count())







