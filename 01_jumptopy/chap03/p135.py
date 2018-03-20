#coding: cp949
#for i in range(2,10):
#    for j in range(1,10):
#        print(i*j,end=" ")
#    print('')

print("<<구구단 출력 프로그램 ver1>>")

#for i in range(2,10):
#    print("* %d단" %i)
#    for j in range(1,10):
#        print("%d*%d=%d"%(i,j,i*j))
#    print("")

select=int(input("출력하고자 하는 단을 입력하세요 : ")

for j in range(1,10):
    print("%d*%d=%d"%(select,j,select*j))
        

