# -*- coding: utf-8 -*-
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
            100: 'SQL Server 2008 R2',
            110: 'SQL Server 2012',
            120: 'SQL Server 2014',
            130: 'SQL Server 2016',
            140: 'SQL Server 2017'}

os.system('sqlcmd -L')
ServerName = input('Имя сервера: ')

myConnStr = 'Provider=SQLNCLI11; Data Source=' + ServerName + '; Initial Catalog=master; User ID=hotel3; Password=123'
myConn = adodbapi.connect(myConnStr)

myCursor = myConn.cursor() # читает данные для БД с выбранного сервера
myCurDB_size = myConn.cursor() # читает размер, занимаемый БД на диске
myCursor.execute('SELECT name, database_id, create_date, compatibility_level  FROM sys.databases')

cprint('{:^25} {:^5} {:>10} {:>15} {:>20}'.format('Имя БД', 'Номер', 'Дата создания', 'Совместимость', 'Размер(Mb)'), 'yellow')
for row in myCursor:
    s_create_date = str(row.create_date)[:10]  # первые 10-ть символов даты
    sovmestim = v_server[row.compatibility_level]
    size_DB = '----'
    if row.name not in ('master','model','msdb','tempdb','ReportServer','ReportServerTempDB', 'RACDemo'):
        myCurDB_size.execute(
            'select size_db = str(sum(convert(dec(17,2),size)) / 128, 10, 2) from ' + row.name + '.dbo.sysfiles')

        size_DB = str(myCurDB_size.fetchone())
    cprint('{:<25} {:<5} {:>10} {:>20} {:^20}'.format(row.name, row.database_id, s_create_date, sovmestim, size_DB[2:12]))













