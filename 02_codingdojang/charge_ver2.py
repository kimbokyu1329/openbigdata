#coding: cp949 
string1= '나이를 입력하세요. : '
#string2= '\n요금은 [{0}]원 입니다\n' 
string3= '귀하의 등급은 [{0}]등급이며 요금은 [{1}]원 입니다.'
string_err='잘못된 나이 입력입니다. 다시 입력해 주세요'

print('-'*30)
print('0~3세(유아) : 무료')
print('4~13세(어린이) : 2000원')
print('14~18세(청소년) : 3000원')
print('19~65세(성인) : 5000원')
print('66세 이상(노인) : 무료')
print('-'*30)

while True: 
    print(string1,end='')
    age_input=int(input())
    
    if age_input < 0 :
        print(string_err)
        continue
    
    elif age_input <=3 :
        age_class='유아'
        charge='무료'
        print(string3.format(age_class,charge))
    elif age_input >=4 and age_input <=13 :
        age_class='어린이'
        charge='2000'
        print(string3.format(age_class,charge))
    elif age_input >= 14 and age_input <=18 :
        age_class='청소년'
        charge='3000'
        print(string3.format(age_class,charge))
    elif age_input >= 19 and age_input <= 65 :
        age_class='성인'
        charge='5000'
        print(string3.format(age_class,charge))
    else :
        age_class='노인'
        charge='무료'
        print(string3.format(age_class,charge))















