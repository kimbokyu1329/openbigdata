#coding: cp949 
string1= '���̸� �Է��ϼ���. : '
string2= '\n����� [{0}]�� �Դϴ�\n' 

while True:
    print('0~3�� : ����')
    print('4~13�� : 2000��')
    print('14~18�� : 3000��')
    print('19~65�� : 5000��')
    print('66�� �̻� : ����')
    print(string1,end='')
    age_input=int(input())
    if age_input <=3 :
        print(string2.format('����'))
    elif age_input >=4 and age_input <=13 :
        print(string2.format('2000'))
    elif age_input >= 14 and age_input <=18 :
        print(string2.format('3000'))
    elif age_input >= 19 and age_input <= 65 :
        print(string2.format('5000'))
    else :
        print(string2.format('����'))
















