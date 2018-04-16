import sys
def sum(num1,num2):
    return num1+num2
while True:
    num=input("숫자를 2개 입력하세요 : ").split()
    for i in range(0,len(num)) :
        if num[i] =="종료":
            sys.exit()
    try:
        num1=int(num[0])
    except ValueError :
        print("죄송합니다. 첫번째 입력이 '{0}'입니다. 숫자를 입력하세요".format(num[0]))
    try:
        num2=int(num[1])
    except ValueError :
        print("죄송합니다. 두번째 입력이 '{0}'입니다. 숫자를 입력하세요".format(num[1]))
    else:
        print(sum(num1,num2))

