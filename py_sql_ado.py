# -*- coding: utf-8 -*-
'''
Проба подключиться в SQL серверу через драйвер ADO
'''
import adodbapi

myhost = ".\SQLEXPRESS"
mydatabase = "h3_pr"
myuser = "hotel3"
mypassword = "123"

# connStr = "Provider=SQLOLEDB; Data Source= %s; Initial Catalog=%s; User ID=%s; Password=%s"
# myConnStr = connStr % (myhost, mydatabase, myuser, mypassword)
myConnStr = "Provider=SQLNCLI11; Data Source=.\SQLEXPRESS; Initial Catalog=h3_prot; User ID=hotel3; Password=123"
print(myConnStr)
myConn = adodbapi.connect(myConnStr)

myCursor = myConn.cursor()
try:
	myCursor.execute('select size_db = str(sum(convert(dec(17,2),size)) / 128, 10, 2) from ' + mydatabase + '.dbo.sysfiles')
	for row in myCursor:
		print(row)
except Exception as err:
	print('Ошибка', err)


