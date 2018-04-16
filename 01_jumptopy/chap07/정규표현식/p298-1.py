import re
p=re.compile("abc")  # "" 안의 모든글자가 포함된 글자로  시작하는
m=p.match('abc')
print(m)
m=p.match('abcdefdasf')
print(m)
m=p.match('ab')  #none
print(m)
