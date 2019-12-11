''' Пример выполнения команд операционной системы
    Поиск всех серверов в сети и
    вывод списка БД на выбранном сервере.
'''

import os
import adodbapi
from termcolor import colored, cprint  # Цветной терминал
# Таблица соответствия версии сервера и его названия
# взято отсюда https://docs.microsoft.com/ru-RU/
#              sql/relational-databases/system-catalog-views/sys-databases-transact-sql?view=aps-pdw-2016
v_server = {90: 'SQL Server 2008',
			100: 'SQL Server 2008',
            110: 'SQL Server 2012',
            120: 'SQL Server 2014',
            130: 'SQL Server 2016',
            140: 'SQL Server 2017'}

os.system('sqlcmd -L')
ServerName = input('Имя сервера: ')

myConnStr = 'Provider=SQLNCLI11; Data Source=' + ServerName + '; Initial Catalog=master; User ID=hotel3; Password=123'
myConn = adodbapi.connect(myConnStr)

myCursor = myConn.cursor()
myCursor.execute('SELECT name, database_id, create_date, compatibility_level  FROM sys.databases')

cprint('{:^25} {:<5} {:>10} {:>15}'.format('Имя БД', 'Номер', 'Дата создания', 'Совместимость'), 'yellow')
for row in myCursor:
    s_create_date = str(row.create_date)[:10]  # первые 10-ть символов даты
    sovmestim = v_server[row.compatibility_level]
    cprint('{:<25} {:<5} {:>10} {:>15}'.format(row.name, row.database_id, s_create_date, sovmestim ))
