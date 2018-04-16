import re

p=re.compile("[a-z][0-9]-case")
m=p.match("a1-case")
print(m)