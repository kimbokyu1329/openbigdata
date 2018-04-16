import sys
path="poll.txt"
def read_content():
   f=open(path,'r')
   global poll_list
   poll_list=f.readlines()
def current():
    print('현재 누적 응답 현황')
    for i in range (0,len(poll_list)):
        print(poll_list[i].rstrip())
def put():
    f=open(path,'a')
    f.write(data)

while True:
    try:
        read_content()
        current()
        reason=input('프로그램이 왜 좋으세요? ("종료" 입력시 프로그램 종료) : ')
        if reason == '종료' :
            break
        name = input('응답자의 이름을 입력하세요 : ')
        print("설문에 응답해 주셔서 감사합니다\n")
        data='\n['+name+'] '+reason
        put()
    except FileNotFoundError:
        print("기존 poll.txt 파일을 찾을 수 없습니다. 아래 중 선택하세요. : ")
        sel_menu=int(input("1. 종료 , 2. 새로운 파일 생성, 3. 변경된 파일 경로 입력"))
        print(sel_menu)
        if sel_menu ==1 :
            sys.exit()
        elif sel_menu ==2 :
            f=open(path,'w')
            f.close()
        elif sel_menu ==3 :
            print('1')
            path = input("변경된 경로를 입력하세요 :")
            path = path+"\\poll.txt"