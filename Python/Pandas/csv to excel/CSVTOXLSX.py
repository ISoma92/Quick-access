import pandas as pd 

df = pd.read_csv("employment_status.csv")

with pd.ExcelWriter("employment_status.xlsx") as writer:
    df.to_excel(writer, sheet_name="Sheet1", index=False)