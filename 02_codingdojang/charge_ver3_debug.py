#coding: cp949 
string1= '���̸� �Է��ϼ���. : '
#string2= '\n����� [{0}]�� �Դϴ�\n' 
string3= '������ ����� [{0}]����̸� ����� [{1}]�� �Դϴ�.'
string_err='�߸��� ���� �Է��Դϴ�. �ٽ� �Է��� �ּ���'
string4= '����� �Է� �ϼ���(����=0)'
string_correct='"�����մϴ�. Ƽ���� �����մϴ�."'
string_excess='"�����մϴ�. Ƽ���� �����ϰ� �Ž����� [{0}]���� ��ȯ �մϴ�."'
string_less='"[{0}]�� ���ڶ��ϴ�. �Է��Ͻ� [{1}]���� ��ȯ�մϴ�."' 




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
        charge_free=0
        print(string3.format(age_class,charge))
        print(string4,end='')
        charge_input=int(input())
        
        if charge_input == charge_free  :
            print(string_correct)
        elif charge_input > charge_free :
            print(string_excess.format(charge_input))
