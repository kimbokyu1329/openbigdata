#!/usr/bin/env python3
import csv
import sqlite3
import sys

# path to and name of csv input file

input_file = sys.argv[1]

#create an in-memory sqlit3 database
#create a table called suppliers with five attributes

con = sqlite3.connect("Suppliers.db")
c = con.cursor()
create_table = """create table if not exists Suppliers
                 (Supplier_Name varchar(20),
                 Invoice_Number varchar(20),
                 Part_Name varchar(20),
                 Cost float,
                 Purchase_Date DATE)"""

c.execute(create_table)
con.commit()

file_reader = csv.reader(open(input_file,'r'),delimiter=',')
header = next(file_reader,None)
for row in file_reader :
    data=[]
    for column_index in range(len(header)):
        data.append(row[column_index])
    print(data)
    c.execute("insert into Suppliers values (?,?,?,?,?)", data)
con.commit()

output = c.execute("select * from suppliers")
rows = output.fetchall()
for row in rows :
    output = []
    for column_index in range(len(row)) :
        output.append(str(row[column_index]))
    print(output)

