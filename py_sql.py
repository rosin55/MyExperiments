'''
Чтение данных из таблицы hotel3.pers MS SQL
'''
import sys
from termcolor import colored, cprint # Цветной терминал
import pyodbc
server = 'localhost\\sqlexpress'
database = 'h3_prot'
username = 'hotel3'
password = '123'
driver = '{SQL Server}'
conn_str = 'DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password
print(conn_str)
cnxn = pyodbc.connect(conn_str)
cursor = cnxn.cursor()
cursor.execute("SELECT TOP(10) * FROM pers")
row = cursor.fetchone()
status = ''
cprint('{:>5} {:<6} {:<10} {:<15} {:<10} {:<10} {:<10}'
	  .format('Код', 'Логин', 'Пароль', 'Фамилия', 'Имя', 'Отчество', 'Статус'), 'yellow', 'on_white')
for row in cursor:
	if row.AdmMsk:
		status = 'Используется'
	if row.AdmCod%2:
		color_of_fone = 'reverse'
	cprint('{:>5} {:<6} {:<10} {:<15} {:<10} {:<10} {:<10}'
		.format(row.AdmCod, row.AdmLogin, row.AdmPwd, row.AdmNam1, row.AdmNam2, row.AdmNam3, status), 'yellow')





