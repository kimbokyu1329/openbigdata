count = 0
while True :
    name = input("안녕하세요. 이름을 입력하세요 (종료 -1) : ")
    count +=1
    if name =='-1' :
        break
    if count ==1 :
        print("Hi {0}!! You ar 1st person come here!".format(name))
    elif count ==2 :
        print("Hi {0}!! You ar 2nd person come here!".format(name))
    elif count ==3 :
        print("Hi {0}!! You ar 3rd person come here!".format(name))
    elif count <=10 :
        print("Hi {0}!! You ar {1}th person come here!".format(name,count))
    else :
        print("Sorry {0}. The event is closed beacuase You are {1}th person come here".format(name,count))