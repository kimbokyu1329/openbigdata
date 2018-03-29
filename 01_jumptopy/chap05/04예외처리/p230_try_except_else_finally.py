num1 , num2 = input("두개의 숫자를 입력하세요 : ").split()

try :
    f = open("나없는파일2","r")
    result = int(num1)/int(num2)
except FileNotFoundError as e:
    print("파일을 찾을 수 없습니다")
    print("System error message :" + str(e))
    is_calculate=False
except ZeroDivisionError as e:
    print("연산을 할 수 없습니다.")
    print("System error message :" + str(e))
    is_calculate= False
else :
    is_calculate=True
finally:
    try :
        f.close()
    except:
        pass

if is_calculate:
    print("%s / %s =%d " %(num1,num2,result))
