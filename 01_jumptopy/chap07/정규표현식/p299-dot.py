import re

p=re.compile("a.b")  # 3글자만
m=p.match("a3b")
print(m)

p=re.compile("330.py")
m=p.match("330.py")
m=p.match("330_py")  # 원하는 결과가 아님에도 매칭이됨
print(m)

p=re.compile("330[.]py")  # 3글자만
m=p.match("330.py")
print(m)
m=p.match("330_py")  # 매칭안됨
print(m)
