#coding: cp949
x=0
y=1
z=0

print("x:" + str(x) + " y:" +str(y)) #z�� ����� �� �ֵ��� ���˽�Ʈ������ ���� 
print("="*40)

if x or y :
    print(" x or y is true?")
    print("TRUE! if statement block ����")
else :
    print(" x or y is true?")
    print("false ���� �Ҹ���")
print("="*40)

if x and y :
    print(" x and y is true?")
    print("TRUE! if statement block ����")
else :
    print(" x and y is true?")
    print("false ���� �Ҹ���")
print("="*40)

if not x:
    print(" not x  is true? ")
    print("TRUE! if statement block ����")
else :
    print(" not x is true? ")
    print("false ���� �Ҹ���")
print("="*40)

if not y:
    print(" not y  is true? ")
    print("TRUE! if statement block ����")
else :
    print(" not y  is true? ")
    print("false ���� �Ҹ���")
print("="*40)

if x and y and z : 
    print("x and y and z : ���� ����")
else :
    print("x and y and z : ���� �Ҹ���")

if x or y or z :
    print("x or y or z : ���� ����")
else :
    print("x or y or z : ���� �Ҹ���")







