#coding: cp949 
string1= '���̸� �Է��ϼ���. : '
#string2= '\n����� [{0}]�� �Դϴ�\n' 
string3= '������ ����� [{0}]����̸� ����� [{1}]�� �Դϴ�.'
string_err='�߸��� ���� �Է��Դϴ�. �ٽ� �Է��� �ּ���'

print('-'*30)
print('0~3��(����) : ����')
print('4~13��(���) : 2000��')
print('14~18��(û�ҳ�) : 3000��')
print('19~65��(����) : 5000��')
print('66�� �̻�(����) : ����')
print('-'*30)

while True: 
    print(string1,end='')
    age_input=int(input())
    
    if age_input < 0 :
        print(string_err)
        continue
    
    elif age_input <=3 :
        age_class='����'
        charge='����'
        print(string3.format(age_class,charge))
    elif age_input >=4 and age_input <=13 :
        age_class='���'
        charge='2000'
        print(string3.format(age_class,charge))
    elif age_input >= 14 and age_input <=18 :
        age_class='û�ҳ�'
        charge='3000'
        print(string3.format(age_class,charge))
    elif age_input >= 19 and age_input <= 65 :
        age_class='����'
        charge='5000'
        print(string3.format(age_class,charge))
    else :
        age_class='����'
        charge='����'
        print(string3.format(age_class,charge))















