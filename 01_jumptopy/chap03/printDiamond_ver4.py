#coding: cp949
blank=" "
star="*"
pipe="|"

print("마름모 출력 프로그램 ver3.0")
while True:

    a=int(input("홀수를 입력 하세요. (0 <- 종료) : "))
    b=a//2+1
    i=0
    ri=b
   
    if a==0 :
        break
    elif a%2==0:
        print("Error! 홀수만 입력 할 수 있습니다")
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











            
