import pymssql

try:
    conn = pymssql.connect(
        server='DESKTOP-S07K9GM',
        user='DESKTOP-S07K9GM\Szofi',
        database='HomeDb'
    )
    cursor = conn.cursor(as_dict=True)
    cursor.execute('SELECT * FROM [dbo].[Excel2SQLAuto]')
    print(cursor.fetchall())
except pymssql.OperationalError as e:
    print(f"OperationalError: {e}")
except Exception as e:
    print(f"Error: {e}")
finally:
    if 'conn' in locals() and conn:
        conn.close()