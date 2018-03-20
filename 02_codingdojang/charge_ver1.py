#coding: cp949 
string1= '나이를 입력하세요. : '
string2= '\n요금은 [{0}]원 입니다\n' 

while True:
    print('0~3세 : 무료')
    print('4~13세 : 2000원')
    print('14~18세 : 3000원')
    print('19~65세 : 5000원')
    print('66세 이상 : 무료')
    print(string1,end='')
    age_input=int(input())
    if age_input <=3 :
        print(string2.format('무료'))
    elif age_input >=4 and age_input <=13 :
        print(string2.format('2000'))
    elif age_input >= 14 and age_input <=18 :
        print(string2.format('3000'))
    elif age_input >= 19 and age_input <= 65 :
        print(string2.format('5000'))
    else :
        print(string2.format('무료'))
















