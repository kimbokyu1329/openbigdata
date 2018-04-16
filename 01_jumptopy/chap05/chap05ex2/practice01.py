while True :
    age=int(input("나이를 입력하세요 (종료 : -1):"))
    if age < 3 and age>=0 :
        print("영화 입장권 가격은 무료입니다\n")
    elif age >=3 and age <=12 :
        print("영화 입장권 가격은 10$ 입니다\n")
    elif age >12  :
        print("영화 입장권 가격은 15$ 입니다\n")
    elif age == -1 :
        break
    else :
        print ("잘 못된 나이입력입니다. 다시 입력해주세요 \n")