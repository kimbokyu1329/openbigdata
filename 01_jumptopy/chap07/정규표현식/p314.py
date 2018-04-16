import re
p=re.compile("Crow|Servo")
m=p.match("Crow") # match
print(m)

m=p.match("Servo")
print(m)

p=re.compile("short$")
m=p.search("life is too short")
print(m)