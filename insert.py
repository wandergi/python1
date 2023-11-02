import sqlite3

conn = sqlite3.connect('example.db')

print("Opened database successfully")

conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(1, 'EMOBILIS', 7, 'WESTLANDS', 25000.00)")

conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(2, 'EMOBILIS', 7, 'WESTLANDS', 45000.00)")

conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(3, 'ORACLE', 10, 'MICROSOFT', 75000.00)")

conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(4, 'SAFARICOM', 3, 'EASTLANDS', 35000.00)")

conn.commit()
print("Records created successfully")
conn.close()