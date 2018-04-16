import re
p=re.compile("<.*?>")
m=p.match("<aa><bb>adsfdsaf</aa></bb>").group()
print(m)