import re
p=re.compile('aaa.bbb')
dest_str="""aaa
bbb"""
m=p.match(dest_str)  # not match
print(m)

p=re.compile("aaa.bbb",re.DOTALL)
m=p.match(dest_str)
print(m)

p=re.compile("[a-z]+",re.I)
m=p.match("python")
m=p.match("Python")
m=p.match("PYTHON")
print(m)
