import openpyxl
import pytds

wb = openpyxl.load_workbook('Fetched data.xlsx')
sheet = wb.active


conn = pytds.connect(
    server='DESKTOP-S07K9GM',
    database='HomeDb',
    user='Szofi',
    auth=pytds.login.SspiAuth(),
    autocommit=True
)
cursor = conn.cursor()


cursor.execute('SELECT * FROM Excel2SQLwithTXT')
for row in cursor:
    sheet.append(list(row)) 

wb.save('Fetched data.xlsx')   
wb.close() 