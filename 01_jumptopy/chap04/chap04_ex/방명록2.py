f=open('방명록.txt','r')
d=open('방명록.txt','a')
visit_book=f.readlines()
visit_check=[]
# visit_check2=[]
for i in range (0,len(visit_book)):
    visit_check.append(visit_book[i].rstrip().split()[0])
    # visit_check2.extend(visit_check[i].split())
print(visit_book)
print(visit_check)

def search_visitor():
     if name in visit_check :
         print ("{0}님 다시 방문해 주셔서 감사합니다. 즐거운 시간 되세요".format(name))
     elif name not in visit_check :
         name_input=name +' '
         visitor_birth=str(input("생년월일을 입력하세요 (예 : 801212) "))
         visitor_birth_input=visitor_birth+'\n'
         d.write(name_input)
         d.write(visitor_birth_input)
         print("반갑습니다 {0}님 즐거운 시간 되세요".format(name))

name = input("이름을 입력하세요 : ")
search_visitor()


