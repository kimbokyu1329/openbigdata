import re
p=re.compile("ab?c")   # + 앞의 . (=아무거나)가  1번이상 반복되는 것을 의미함
m=p.match("abc") #match
m2=p.match("ac") #match
print(m)
print(m2)
