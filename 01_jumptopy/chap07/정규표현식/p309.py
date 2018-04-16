import re
p=re.compile('hello\s\w') # 문자열 전체에서 hello\s\w 형식을 모두찾음
dest_str="hello my python hello world!"
m=p.findall(dest_str)
print(m)
p=re.compile('^hello\s\w')  # ^ 문자열 전체의 처음이 hello\s\w로 시작한다면 그것 출력
dest_str="hello my python hello world!"
m=p.findall(dest_str)
print(m)
