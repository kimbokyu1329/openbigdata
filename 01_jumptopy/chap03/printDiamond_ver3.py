#coding: cp949
print("������ ��� ���α׷� ver1.0")

while True:

    a=int(input("Ȧ���� �Է� �ϼ���. (0 <- ����) : "))
    if a==0 :
        break
    elif a%2==0:
        print("Error! Ȧ���� �Է� �� �� �ֽ��ϴ�")
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
