#coding: cp949
blank=" "
star="*"
pipe="|"

print("������ ��� ���α׷� ver3.0")
while True:

    a=int(input("Ȧ���� �Է� �ϼ���. (0 <- ����) : "))
    b=a//2+1
    i=0
    ri=b
   
    if a==0 :
        break
    elif a%2==0:
        print("Error! Ȧ���� �Է� �� �� �ֽ��ϴ�")
        continue
    
    print(blank + "-"*a + blank)
    while True:
        i+=1
        print(pipe
                +blank*(b-i) 
                +star*(2*i-1)
                +blank*(b-i)
                +pipe)
        if b == i :
            break
        
    while True:
        ri-=1
        print(pipe+
                blank*(b-ri)
                +star*(2*ri-1)
                +blank*(b-ri)
                +pipe)
        if ri ==1 :
            break
    print(blank + "-"*a + blank)











            
