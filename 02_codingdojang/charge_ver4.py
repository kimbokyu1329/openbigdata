#coding: cp949 
string1= '\n���̸� �Է��ϼ���. : '
#string2= '\n����� [{0}]�� �Դϴ�\n' 
string3= '������ ����� [{0}]����̸� ����� [{1}]�� �Դϴ�.'
string_err='�߸��� ���� �Է��Դϴ�. �ٽ� �Է��� �ּ���'
string4= '\n����� �Է� �ϼ���(����=0): '
string_correct='"�����մϴ�. Ƽ���� �����մϴ�."\n'
string_excess='"�����մϴ�. Ƽ���� �����ϰ� �Ž����� [{0}]���� ��ȯ �մϴ�."\n'
string_less='"[{0}]���� ���ڶ��ϴ�. �Է��Ͻ� [{1}]���� ��ȯ�մϴ�."\n' 
string_charge_type= '��� ������ �����ϼ���. (1:����, 2: ���� ���� �ſ�ī��): '
string_card_discount='(���� �ݾ��� 10%% ����, 60~65�� ����� �߰� 5%% ����)'
string_card_payment='[{0}]�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�.'

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
        charge=0
        print(string3.format(age_class,charge))
        print(string_correct)
        continue
    elif age_input >=4 and age_input <=13:
        age_class='���'
        charge=2000
    elif age_input >= 14 and age_input <=18 :
        age_class='û�ҳ�'
        charge=3000
    elif age_input >= 19 and age_input <= 65 :
        age_class='����'
        charge=5000
    else :
        age_class='����'
        charge=0
        print(string3.format(age_class,charge))
        print(string_correct)
        continue
    print(string3.format(age_class,charge))
    print(string_charge_type)
    charge_type=int(input())
    if charge_type==1 :
        print(string4,end='')
        charge_input=int(input())
        if charge_input == charge :
            print(string_correct)
        elif charge_input > charge :
            print(string_excess.format(charge_input-charge))
        else :
            print(string_less.format(charge-charge_input,charge_input))
    else : 
        print(string_card_discount)
        if age_input >= 60 and age_input <= 65 :
            print(string_card_payment.format(charge*0.85))
        else :
            print(string_card_payment.format(int(charge*0.9)))


