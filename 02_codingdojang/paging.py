#coding: cp949

string1='�ѰǼ�(m): '
string2='�� �������� ������ �Խù� ��(n) (�� n�� 1���� ũ�ų� ����. n >=1): '
m=int(input(string1))
n=int(input(string2))

page=m//n 
if m%n == 0:
    print(page)
elif m%n !=0:
    print(page + 1)
