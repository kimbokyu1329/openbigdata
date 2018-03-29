num1 , num2 = input("두개의 숫자를 입력하세요 : ").split()
is_calculate = True

try :
    f = open("나없는파일","r")
    result = int(num1)/int(num2)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다")
    is_calculate=False
except ZeroDivisionError:
    print("연산을 할 수 없습니다.")
    is_calculate= False


if is_calculate:
    print("%s / %s =%d " %(num1,num2,result))
