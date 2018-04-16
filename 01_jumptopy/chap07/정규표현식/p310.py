import re
p=re.compile('^python\s\w+',re.MULTILINE) # ^의 판단을 라인의 시작에서 하기위한 멀티라인 옵션
dest_str="""python one python debug  
life is too short 
python two
you need python
python three"""
m=p.findall(dest_str)
print(m)
