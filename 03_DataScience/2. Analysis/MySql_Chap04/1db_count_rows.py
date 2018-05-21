#!/usr/bin/env python3
import sqlite3

con = sqlite3.connect(':memory:')
query = """ CREATE TABLE sales 
            (customer varchar(20),
            product varchar(40),
            amount float,
            date date)"""
con.execute(query)
con.commit()

data = [('Richard Lucas' , 'Notepad',2.50,'2014-01-02'),
        ('Jenny KIm','Binder',4.15,'2014-01-15'),
        ('Svetlana Crow','Printer',155.75,'2014-02-03'),
        ('Stephen Randolph','Computer',679.40,'2014-02-20')]
statement = "insert into sales values(?,?,?,?)"
con.executemany(statement,data)
con.commit()

cursor =con.execute("select * from sales")
rows = cursor.fetchall()

row_counter = 0

for row in rows :
    print(row)
    row_counter +=1
print("Number of rows : {}".format(row_counter))