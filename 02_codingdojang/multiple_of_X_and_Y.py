#coding: cp949
Z=10000

print('-'*30)
print('X*Y�� n ����� ���α׷�')
print('-'*30)
while True:
    X=int(input('X�� ���� �Է��ϼ���'))
    Y=int(input('Y�� ���� �Է��ϼ���'))
    mul=X*Y
    range_n=Z//mul
    n=int(input('{0}*{1}�� ����  �� ������� ���Ͻðڽ��ϱ� (0=����) :'.format(X,Y)))
    if n == 0 :
        break
    if n > range_n:
        print('������ �ʰ� �Ͽ����ϴ�. (n={0}~{1})'.format(0,range_n))
    else: 
        print(mul*n)



