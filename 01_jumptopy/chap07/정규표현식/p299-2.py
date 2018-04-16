import re
p=re.compile('[0-9]')
m=p.match("a") #none
print(m)
m=p.match("1aasdfsadfsadfaa")
print(m)
