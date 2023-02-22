import pyodbc

# DRIVER_NAME = 'SQL SERVER'
# server = 'localhost'
# SERVER_NAME = 'DESKTOP-KQ740OS'
# DATABASE_NAME = 'sample'

# cnxn_str = ("Driver={SQL Server Native Client 11.0};"
#             "Server=DESKTOP-KQ740OS;"
#             "Database=sample;"
#             "Trusted_Connection=yes;")
# cnxn = odbc.connect(cnxn_str)

conx_string = 'DRIVER={SQL Server}; SERVER=DESKTOP-KQ740OS; Database=sample; TRUSTED_CONNECTION=yes'
conx = pyodbc.connect(conx_string);

query = "select * from Employee"
cursor = conx.cursor()
cursor.execute(query)
data = cursor.fetchall
columns = [column[0] for column in cursor.description]
# print(dict(data))


conx.close()