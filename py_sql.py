'''
Чтение данных из таблицы hotel3.pers MS SQL
'''
import pyodbc
server = 'localhost\\sqlexpress'
database = 'h3_prot'
username = 'hotel3'
password = '123'
driver= '{SQL Server}'
conn_str = 'DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password
print(conn_str)
cnxn = pyodbc.connect(conn_str)
cursor = cnxn.cursor()
cursor.execute("SELECT TOP(10) * FROM pers")
row = cursor.fetchone()
print('{:>5} {:<10} {:<10} {:<15} {:<10} {:<10} {:<10}'
	  .format('Код', 'Логин', 'Пароль', 'Фамилия', 'Имя', 'Отчество', 'Статус'))
for row in cursor:
	if row.AdmMsk:
		Status = 'Используется'
	print('{:>5} {:<10} {:<10} {:<15} {:<10} {:<10} {:<10}'
		  .format(row.AdmCod, row.AdmLogin, row.AdmPwd, row.AdmNam1, row.AdmNam2, row.AdmNam3, Status))





