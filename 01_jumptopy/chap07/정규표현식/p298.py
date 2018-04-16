import re
p=re.compile('[abc]')   # [] 안의 첫글자로 시작하는 것을 매칭
m=p.match("a")
print(m)
m=p.match("before")
print(m)
m=p.match("dude")    # none
print(m)
m=p.match('[') #none
print(m)
m=p.match("glob") #none
print(m)