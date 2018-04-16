import re
p=re.compile('[a-z]')
m=p.match("a")
print(m)
m=p.match("before")
print(m)
m=p.match("dude")
print(m)
m=p.match("glob")
print(m)
m=p.match("A")  #none
print(m)
