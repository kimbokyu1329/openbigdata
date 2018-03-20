#coding: cp949

coffee =10
money=300

while money:
    print("돈을 받았으니 커피를 줍니다")
    coffee-=1

    print("남은 커피의 양은 {0}개입니다".format(coffee))

    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 종료합니다.")
        break
