import re
p=re.compile('[0-9]')
m=p.match("7")
print(m)

p=re.compile('\d')  #숫자매칭
m=p.match("7")
print(m)

p=re.compile('\D')  #숫자가 아닌것 매칭
m=p.match("7")
print(m)

p=re.compile('\s')
m=p.match(" ")
print(m)

p=re.compile('\S')  # 공백말고 아무거나 있기만하면
m=p.match(" ")
a=p.match("turoept23p4")
print(m)
print(a)

p=re.compile('[a-zA-Z0-9]')  # 대소문자,숫자 면 매칭
p=re.compile('[\w]')  # 대소문자,숫자 면 매칭
m=p.match("DF213")
print(m)
m=p.match("!") # none
print(m)
p=re.compile('[\W]')  # 대소문자,숫자 아니면 매칭
m=p.match("!")
print(m)
