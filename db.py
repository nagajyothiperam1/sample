
#Single rows are inserted using execute and multiple rows using executeMany method of created cursor object.
import sqlite3
#db connection
con = sqlite3.connect('D:\\TEST.db')
cursor = con.cursor()

#query
#sql1 = 'CREATE TABLE EMP (Id Int,Name Varchar)'
#sql3='DROP TABLE EMP'
#sql2='PRAGMA table_info(emp);'

#executing query
#cursor.execute(sql2)

# #message output
# print(cursor.fetchall())

#===inserting data===
# val=(1,'abc')
# sql='INSERT INTO EMP VALUES (?,?)'
# try:
	# cursor.execute(sql,val)
	# con.commit()
	# print("inserted")
# except Exception as e:
	# print("error",str(e))
	# con.rollback()
	
#===selecting data===	
sqls='''
SELECT * FROM EMP
'''
try:
	cursor.execute(sqls)
	print("selected")
except:
	print("error")
	
record=cursor.fetchone()
#for records in record:
print(record)

#closing connection
con.close()