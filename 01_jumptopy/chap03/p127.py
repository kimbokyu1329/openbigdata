#coding: cp949

coffee=10
while True :
    money=int(input("\n돈을 넣으세요: "))

    if money==300:
        print("커피가 나옵니다. 잠시만 기다려주세요.")
        coffee-=1
    
    elif money>300:
        print("커피가 나옵니다. 잠시만 기다려주세요. \n거스름돈 {0}원이 반환됩니다.".format(money -300))
        coffee-=1
    
    else:
        print("돈이 부족하여 반환됩니다.")
    
    print("남은 커피의 양은 %d개 입니다."% coffee) #indentation while에 맞춰서 항상 커피양이 출력되도록함
    
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
    





