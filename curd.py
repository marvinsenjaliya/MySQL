import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
)
print(mydb.connection_id)
cursor = mydb.cursor()

class MYSQL:

    def __init__(self):
        pass

    def database(self):
        query='create database Employee'

    def create(self):
        query='CREATE TABLE BRANCH(id integer(2),name varchar(20),branch varchar(20),salary integer(7))'
       # cursor.execute(query)

    def insert(self):
        query='INSERT INTO BRANCH(id,name,branch,salary) values(%s,%s,%s,%s)'
        d1=((1,'marvin','dataEngg',70000),(2,'Akshay','dataEngg',12000),(3,'Nikunj','Automation',15000))
        cursor.executemany(query,d1)
        mydb.commit()

    def printInfo(self):
        query='select * from BRANCH'
        cursor.execute(query)
        result = cur.fetchall()
        for data in result:
            print(data)

    def update(self):
        query='update BRANCH set salary = salary+2000 WHERE salary>12000'
        cursor.execute(query)
        mydb.commit()

    def delete(self):
        query='DELETE FROM BRANCH where name =Nikunj'
        cursor.execute(query)

    def drop(self):
        query='DROP DATABASE'
        cursor.execute(query)


if __name__== "__main__":
    operation=MYSQL()
    operation.create()
    operation.insert()
    operation.update()
    operation.delete()


