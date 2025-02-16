import openpyxl
import pyodbc

wb = openpyxl.load_workbook('Fetched data.xlsx')
sheet = wb.active


conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=DESKTOP-S07K9GM;'
    'DATABASE=HomeDb;'
    'Trusted_Connection=yes;'
    #'UID=your_username;'    Not required if using Windows Authentication on a home SQL Server
    #'PWD=your_password'     Not required if using Windows Authentication on a home SQL Server
)
cursor = conn.cursor()


cursor.execute('SELECT * FROM Excel2SQLwithTXT')
for row in cursor:
    sheet.append(list(row)) 

wb.save('Fetched data.xlsx')   
wb.close() 