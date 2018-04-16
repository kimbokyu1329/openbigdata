import re

p=re.compile("ca*t")  # * 앞의 a가 0 이상 반복되면 매칭
m=p.match("ct")
print(m)
m=p.match("cdft")
print(m)
