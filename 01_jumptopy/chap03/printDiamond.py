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
    for c in range(0,b):
        print(" "*(b-c)+"*"*(2*c+1))        
    for d in range(1,b):
        print(" "*(d+1)+"*"*(a-2*d))
