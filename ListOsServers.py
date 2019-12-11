''' Пример выполнения команд операционной системы
    Поиск всех серверов в сети и
    вывод списка БД на выбранном сервере.
'''

import os
import adodbapi

os.system('sqlcmd -L')
ServerName = input('Имя сервера: ')

myConnStr = 'Provider=SQLNCLI11; Data Source=' + ServerName + '; Initial Catalog=h3_prot; User ID=hotel3; Password=123'
myConn = adodbapi.connect(myConnStr)

myCursor = myConn.cursor()
myCursor.execute('SELECT name, database_id, create_date  FROM sys.databases')

for row in myCursor:
    print(row)

