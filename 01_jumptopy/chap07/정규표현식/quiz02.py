import re
p=re.compile(".+[.]...")   # + 앞의 . (=아무거나)가  1번이상 반복되는 것을 의미함
m=p.match("a.txt")
m2=p.match("bk3.py")
m3=p.match("python.doc")
print(m)
print(m2)
print(m3)