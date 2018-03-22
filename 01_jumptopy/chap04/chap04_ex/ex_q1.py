def fib(n) :
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-2) + fib(n-1)


n=int(input('정수 n을 입력하세요 : '))
print("피보나치 수열  %d 번째 값:"%(n+1) + str(fib(n)) )
fiblist=[]
for i in range(0,n+1) :
    fiblist.append(fib(i))

print(fiblist)
