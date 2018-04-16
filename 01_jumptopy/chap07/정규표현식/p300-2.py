import re

p=re.compile("ca{2}t") # {2} 앞의 a가 2번 반복될때만
m=p.match("cat")
print(m)
m=p.match("caat")  #match
print(m)
m=p.match("caaat")
print(m)

p=re.compile("ca?t")
m4=p.match("ct") #match
print(m4)
