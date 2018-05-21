#! /usr/bin/env python3
import csv
import sys
import sqlite3

#path to and name of csv input file
input_file = sys.argv[1]

con=sqlite3.connect(':memory:')
query = """create table if not exists sales 
           (customer varchar(20),
           product varchar(40),
           amount float,
           date date);"""
con.execute(query)
con.commit()

data = [('Richard Lucas' , 'Notepad',2.50,'2014-01-02'),
        ('Jenny KIm','Binder',4.15,'2014-01-15'),
        ('Svetlana Crow','Printer',155.75,'2014-02-03'),
        ('Stephen Randolph','Computer',679.40,'2014-02-20')]
for tuple in data:
        print(tuple)
statement = "insert into sales values(?,?,?,?)"

con.executemany(statement,data)
con.commit()

file_reader = csv.reader(open(input_file,'r'),delimiter=',')
header = next(file_reader,None)
for row in file_reader :
        data=[]
        for column_index in range(len(header)):
                data.append(row[column_index])
        print(data)
        con.execute("update sales set amount=?,date=? where customer=?;", data)
con.commit()

output = con.execute("select * from sales")
rows = output.fetchall()
for row in rows :
        output = []
        for column_index in range(len(row)) :
                output.append(str(row[column_index]))
        print(output)

