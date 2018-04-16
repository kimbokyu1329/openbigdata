f=open("poll.txt","a")
while  True :
    reason=input("프로그래밍이 왜 좋으세요? (종료 입력시 프로그램 종료) :")
    if reason == '종료' :
        break
    name = input("응답자의 이름을 입력해 주세요 :")
    print("설문에 응답해 주셔서 감사합니다")
    data= "[" + name + "]" +reason
    f.write(data)
f.close()

