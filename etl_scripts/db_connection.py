import pyodbc

def get_db_connection():
    connection_string = (
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-6CVS8GM\\SQLEXPRESS;'
        'DATABASE=DW_DataShop;'
        'Trusted_Connection=yes;'
    )
    return pyodbc.connect(connection_string)
