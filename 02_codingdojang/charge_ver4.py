#coding: cp949 
string1= '\n나이를 입력하세요. : '
#string2= '\n요금은 [{0}]원 입니다\n' 
string3= '귀하의 등급은 [{0}]등급이며 요금은 [{1}]원 입니다.'
string_err='잘못된 나이 입력입니다. 다시 입력해 주세요'
string4= '\n요금을 입력 하세요(무료=0): '
string_correct='"감사합니다. 티켓을 발행합니다."\n'
string_excess='"감사합니다. 티켓을 발행하고 거스름돈 [{0}]원을 반환 합니다."\n'
string_less='"[{0}]원이 모자랍니다. 입력하신 [{1}]원을 반환합니다."\n' 
string_charge_type= '요금 유형을 선택하세요. (1:현금, 2: 공원 전용 신용카드): '
string_card_discount='(결제 금액의 10%% 할인, 60~65세 장년은 추가 5%% 할인)'
string_card_payment='[{0}]원 결제 되었습니다. 티켓을 발행합니다.'

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
        charge=0
        print(string3.format(age_class,charge))
        print(string_correct)
        continue
    elif age_input >=4 and age_input <=13:
        age_class='어린이'
        charge=2000
    elif age_input >= 14 and age_input <=18 :
        age_class='청소년'
        charge=3000
    elif age_input >= 19 and age_input <= 65 :
        age_class='성인'
        charge=5000
    else :
        age_class='노인'
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


