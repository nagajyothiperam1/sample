
#Single rows are inserted using execute and multiple rows using executeMany method of created cursor object.
import sqlite3
#db connection
con = sqlite3.connect('D:\\TEST.db')
cursor = con.cursor()

#query
sql1 = 'CREATE TABLE EMP (Id Int,Name Varchar)'
#sql3='DROP TABLE EMP'
#sql2='PRAGMA table_info(emp);'

#executing query
# cursor.execute(sql1)

# #message output
# print(cursor.fetchall())
# val=(1,'abc')
# sql='INSERT INTO EMP VALUES (?,?)'
# try:
	# cursor.execute(sql,val)
	# con.commit()
# except Exception as e:
	# print("error",str(e))
	# con.rollback()
sqls="SELECT * FROM EMP;"
try:
	cursor.execute(slqs)
except:
	print('error')
record=cursor.fetchall()
for records in record:
	print(records)

#closing connection
con.close()