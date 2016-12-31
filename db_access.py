import MySQLdb

db = MySQLdb.connect("localhost","root","awi421","mydb")

cursor = db.cursor()

#delete table
cursor.execute("DROP TABLE IF EXISTS product")

#create table
sql = """CREATE TABLE product (
         name char(20) NOT NULL,
         price int)"""

cursor.execute(sql)

sql = """INSERT INTO product (name,price)
         VALUES ('computer','1000')"""

cursor.execute(sql)
db.commit()

sql = "SELECT * FROM product"
cursor.execute(sql)

results = cursor.fetchall()
print results
db.close()
