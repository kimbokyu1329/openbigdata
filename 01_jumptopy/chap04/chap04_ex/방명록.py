f=open('방명록.txt','r')
d=open('방명록.txt','a')
visit_book=f.readlines()
visit_check=[]
visit_check2=[]
for i in range (0,len(visit_book)):
    visit_check.append(visit_book[i].rstrip())
    visit_check2.extend(visit_check[i].split())
print(visit_check2)
check=str(visit_check2)

def search_visitor():
     if check.find(name) >0 :
         print ("{0}님 다시 방문해 주셔서 감사합니다. 즐거운 시간 되세요".format(name))
     elif check.find(name) == -1 :
         name_input=name +' '
         visitor_birth=str(input("생년월일을 입력하세요 (예 : 801212) "))
         visitor_birth_input=visitor_birth+'\n'
         d.write(name_input)
         d.write(visitor_birth_input)
         print("반갑습니다 {0}님 즐거운 시간 되세요".format(name))

name = input("이름을 입력하세요 : ")
print(check.find(name))
search_visitor()


