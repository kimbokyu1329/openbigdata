# py -m pip install mysqlclient
import csv
import MySQLdb
import sys
from datetime import datetime, date

#Path to and name of a csv input file
input_file = sys.argv[1]

#Connect to a mysql database
#con = MySQLdb.connect(host='localhost',port=3306,db='my_suppliers',user='python_training',passwd='python_training')

con = MySQLdb.connect(host='localhost',port=3306,db='my_suppliers',user='open_source',passwd='flsnrtm')
c=con.cursor()

file_reader = csv.reader(open(input_file),delimiter=',')
header = next(file_reader)
for row in file_reader :
    data=[]
    for column_index in range(len(header)):
        if column_index <4 :
            data.append(str(row[column_index]).lstrip('$')\
                        .replace(',','').strip())
        else :
            a_date = datetime.date(datetime.strptime(\
                str(row[column_index]), '%Y-%m-%d'))
            a_date=a_date.strftime('%y-%m-%d')
            data.append(a_date)

    print(data)
    c.execute("""insert into Suppliers values(%s, %s, %s, %s, %s);""",data)
con.commit()

c.execute("select * from Suppliers")
rows = c.fetchall()
for row in rows :
    row_list_output=[]
    for column_index in range(len(row)):
        row_list_output.append(str(row[column_index]))
    print(row_list_output)




