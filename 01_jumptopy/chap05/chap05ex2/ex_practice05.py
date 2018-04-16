import sys
def sum(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
while True:
    num=input("숫자를 2개 입력하세요 : ").split()
    try:
        num[0]=int(num[0])
        num[1]=int(num[1])
        print("두 수의 합",sum(num[0],num[1]))
        print("두 수의 차",sub(num[0],num[1]))
        print("두 수의 곱",mul(num[0],num[1]))
        print("두 수의 제",div(num[0],num[1]))
    except ValueError :
        if num[0] =="종료" or num[1] =="종료" :
            break
        elif not isinstance(num[0],int):
            print("죄송합니다. 첫번째 입력이 '{0}'입니다. 숫자를 입력하세요".format(num[0]))
        else :
            print("죄송합니다. 두번째 입력이 '{0}'입니다. 숫자를 입력하세요".format(num[1]))
    except ZeroDivisionError :
        if num[0] == 0 :
            print("죄송합니다. 첫 번째 입력에서 0을 입력하셨습니다. 분모는 0이 되어서는 않됩니다.")
        elif num[1] == 0 :
            print("죄송합니다. 두 번째 입력에서 0을 입력하셨습니다. 분모는 0이 되어서는 않됩니다.")
