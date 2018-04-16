import re
p=re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m=p.search("park 053-782-1329")
print(m.group(0))
print(m.group(1))
print(m.group(2))
