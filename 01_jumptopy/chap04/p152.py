def say_myself(name,old,man=True):
    print("나의이름은 %s입니다." %name)
    print("나의 나이는 %d살입니다"%old)

    if man :
        print("남자 입니다")
    else:
        print("여자입니다")

say_myself("박응용",27)
say_myself("안철수",56,True)
say_myself("이효리",34,False)