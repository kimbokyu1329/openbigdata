import re

p=re.compile("ca+t") # + 앞의 a가 1번이상 반복될때 매칭
m=p.match("ct")
print(m)
m=p.match("caaaat")
print(m)
