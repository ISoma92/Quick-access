import pandas as pd

df = pd.read_json('sample_users_with_id.json')

## print(df.to_string())

with pd.ExcelWriter("sample_users_with_id.xlsx") as writer:
    df.to_excel(writer, sheet_name="Sheet1", index=False)