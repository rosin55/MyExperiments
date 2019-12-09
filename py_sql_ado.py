'''
Проба подключиться в SQL серверу через драйвер ADO
'''
import adodbapi

myhost = ".\SQLEXPRESS"
mydatabase = "h3_prot"
myuser = "hotel3"
mypassword = "123"

# connStr = "Provider=SQLOLEDB; Data Source= %s; Initial Catalog=%s; User ID=%s; Password=%s"
# myConnStr = connStr % (myhost, mydatabase, myuser, mypassword)
myConnStr = "Provider=SQLNCLI11; Data Source=.\SQLEXPRESS; Initial Catalog=h3_prot; User ID=hotel3; Password=123"
print(myConnStr)
myConn = adodbapi.connect(myConnStr)

myCursor = myConn.cursor()
myCursor.execute('select * from pers')

for row in myCursor:
	print(row)

