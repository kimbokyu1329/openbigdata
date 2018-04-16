import re
p=re.compile('[a-z]+')
m=p.match("python") #match
print(m)
m=p.match("3 python") #not match  3 ,blank
print(m)
m=p.search("python") # match
print(m)
m=p.search("3 python") #match
print(m)

m=p.match("life is too short")  #life 만 match 되어 matching
print(m)
m=p.search("life is too short") # life 만 match 되어 matching
print(m)
m=p.findall("life is too short") # matching 되는 모든 것 리스트로 반환  여기서는 모두 매칭됨
print(m)
result=p.finditer("life is too short")
for r in result :  #match 되는 위치를 알려줌
    print(r)

