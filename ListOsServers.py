''' Пример выполнения коман операционной системы '''

import os
import adodbapi

os.system('sqlcmd -L')
ServerName = input('Имя сервера: ')

conn_string = 'sqlcmd -S' + ServerName + ' -Uhotel3 -P123 -Q "SELECT name, database_id, create_date  FROM sys.databases"'
print(conn_string)
os.system(conn_string)

