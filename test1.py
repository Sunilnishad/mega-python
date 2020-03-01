import pandas as pd

x1 = pd.ExcelFile("name.xlsx")

print(x1.sheet_names)

df = x1.parse("Sheet1")
df.head()