import datetime
import os
# s=datetime.datetime.now()
# print(type(s))
#
#
# print(type(len(os.listdir('.\\'))))
a=['a','b','c','d']
b=['d','d','e','f']
c=[]
for i in range (4) :
    c.append(a[i]+b[i])
print(c)