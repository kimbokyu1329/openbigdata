import re
p=re.compile('\section')
m=p.findall("\section") # not match
print(m)
m=p.findall(" ection") # match
print(m)

p=re.compile(r'\\section')
m=p.findall("\section") # not match
print(m)
m=p.findall(" ection") # match
