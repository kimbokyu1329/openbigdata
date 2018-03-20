def verify_customer(name,old,level='silver'):
    print("고객님의 이름은 %s입니다." %name)
    print("고객님의 나이는 %d살입니다"%old)

    if level == 'silver':
        print("고객님의 등급은 %s입니다\n"%level)
    elif level == "gold":
        print("고객님의 등급은 %s입니다\n"%level)
    elif level == "platinum":
        print("고객님의 등급은 %s입니다\n"%level)


verify_customer("박응용",27,'gold')
verify_customer("안철수",56)
verify_customer("이효리",34,'platinum')