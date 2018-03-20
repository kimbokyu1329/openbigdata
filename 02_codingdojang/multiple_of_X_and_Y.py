#coding: cp949
Z=10000

print('-'*30)
print('X*Y의 n 공배수 프로그램')
print('-'*30)
while True:
    X=int(input('X의 값을 입력하세요'))
    Y=int(input('Y의 값을 입력하세요'))
    mul=X*Y
    range_n=Z//mul
    n=int(input('{0}*{1}에 대한  몇 공배수를 구하시겠습니까 (0=종료) :'.format(X,Y)))
    if n == 0 :
        break
    if n > range_n:
        print('범위를 초과 하였습니다. (n={0}~{1})'.format(0,range_n))
    else: 
        print(mul*n)



