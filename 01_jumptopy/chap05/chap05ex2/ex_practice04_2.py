import sys
def sum(num1,num2):
    return num1+num2
while True:
    num=input("숫자를 2개 입력하세요 : ").split()
    try:
        num[0]=int(num[0])
        num[1]=int(num[1])
    except ValueError :
        if num[0] =="종료" or num[1] =="종료" :
            break
        elif not isinstance(num[0],int):
            print("죄송합니다. 첫번째 입력이 '{0}'입니다. 숫자를 입력하세요".format(num[0]))
        else:
            print("죄송합니다. 두번째 입력이 '{0}'입니다. 숫자를 입력하세요".format(num[1]))
    else:
        print(sum(num[0],num[1]))

