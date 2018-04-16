import re
p = re.compile(".+:")
m = p.search("http://google.com")
print(m)
p = re.compile(".+(?=:)")  # : 을 제외하고 매칭
m = p.search("http://google.com")
print(m)
