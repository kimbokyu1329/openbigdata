import re
p=re.compile('[a-z]-case')
m=p.match("able")
print(m)
m=p.match("a-case")
print(m)
m=p.match("b-case")
print(m)
m=p.match("c-case")
print(m)
m=p.match("c-case asdfsadfsadf")
print(m)
