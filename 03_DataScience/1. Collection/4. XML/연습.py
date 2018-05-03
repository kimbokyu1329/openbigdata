import datetime
import os
# s=datetime.datetime.now()
# print(type(s))
#
#
# print(type(len(os.listdir('.\\'))))
# a=['a','b','c','d']
# b=['d','d','e','f']
# c=[]
# for i in range (4) :
#     c.append(a[i]+b[i])
# print(c)
# str= " 23 3 43435  3243"
# print(str.strip(' '))p
import datetime
yyyymmdd=datetime.datetime.now().strftime('%Y%m%d')
a=datetime.timedelta(minutes=40)
time=(datetime.datetime.now()-a).strftime('%H%M')
print(time)
