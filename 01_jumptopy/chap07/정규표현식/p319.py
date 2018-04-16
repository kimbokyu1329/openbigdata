import re
p=re.compile(r"(\b\w+)\s+\1")
print(p.search("Paris in the the spring the").group())
print(p.findall("Paris in the the spring the kkk kkk"))
print(p.search("Paris in the the spring the kkk kkk").group(0))
