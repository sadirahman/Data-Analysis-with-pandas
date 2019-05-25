import pandas as pd
from pandas import ExcelWriter

def Number_of_line(cell):
    if cell =="None":
        return 'NaN'
    return cell

df = pd.read_excel("C:\\Users\\Sun of sadi\\PycharmProjects\\Pandas\Data\\book1.xlsx", "Sheet1", converters={
      'Number  of line': Number_of_line
})
print(df)
df.to_excel('New_Data.xlsx',sheet_name='book1')
print(df)

print("show Our result:")


Group = df.groupby('Name')
w = ExcelWriter('nam.xlsx')
c = ExcelWriter('count.xlsx')
for Name,name_df in Group:
    print(Name)
    print(name_df)
    Count = name_df.count()
    print(Count)
    Count.to_excel(c, sheet_name='sheet ' + str(Name))
    c.save()
    name_df.to_excel(w, sheet_name='sheet ' + str(Name))
    w.save()









