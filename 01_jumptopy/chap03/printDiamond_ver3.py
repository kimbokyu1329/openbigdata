#coding: cp949
print("마름모 출력 프로그램 ver1.0")

while True:

    a=int(input("홀수를 입력 하세요. (0 <- 종료) : "))
    if a==0 :
        break
    elif a%2==0:
        print("Error! 홀수만 입력 할 수 있습니다")
        continue
    b=a//2+1
    print(" "+"-"*(a+2)+" ")
    for c in range(0,b):
        print("|",end="")
        print(" "*(b-c)+"*"*(2*c+1)+" "*(b-c)+"|")        
    for d in range(1,b):
        print("|",end="")
        print(" "*(d+1)+"*"*(a-2*d)+" "*(d+1)+"|")
    print(" "+"-"*(a+2)+" ")
