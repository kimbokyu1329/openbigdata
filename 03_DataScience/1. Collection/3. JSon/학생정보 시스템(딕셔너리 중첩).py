def fmore_learning_course() :
    course_code=input("강의코드 (예: IB171106, OB0104 ..): ")
    course_name=input("강의명 (예: IOT 빅데이터 실무반): ")
    teacher=input("강사 (예: 이현구): ")
    open_date=input("개강일 (예: 2017-11-06): ")
    close_date=input("종료일 (예: 2018-09-05): ")
    learning_course_list.append(fdic_for_learning_course(close_date,open_date,course_code,course_name,teacher))
def fdic_for_learning_course(close_date,open_date,course_code,course_name,teacher):
    dic={}
    dic["close_date"]=close_date
    dic["open_date"]=open_date
    dic["course_code"]=course_code
    dic["course_name"]=course_name
    dic["teacher"]=teacher
    return dic
def fdic_for_total_course(list_learnig,num_of_learned_course):
    dic={}
    dic["learning_course_info"]=list_learnig
    dic["num_of_learned_course"]=num_of_learned_course
    return dic
def fdic_for_per_std(std_addr,std_id,std_age,std_name,total_course_dic):
    dic={}
    dic["address"] =std_addr
    dic["student_ID"] =std_id
    dic["student_age"] =std_age
    dic["student_name"] =std_name
    dic["total_course_info"] = total_course_dic
    return dic
def fput_std_dic():
    total_course_dic=fdic_for_total_course(learning_course_list,num_of_learned_course)
    std_dic=fdic_for_per_std(std_addr,std_id,std_age,std_name,total_course_dic)
    course_system_list.append(std_dic)
    print(course_system_list)
###############search
def fread_std(i):
    global course_system_list
    print("*학생 ID: "+course_system_list[i].get('student_ID'))
    print("*학생 이름: "+course_system_list[i].get('student_name'))
    print("*나이: "+course_system_list[i].get('student_age'))
    print("*주소: "+course_system_list[i].get('address'))
    print("*수강정보: ")
    print(" +과거 수강 횟수: "+course_system_list[i].get('total_course_info').get('num_of_learned_course'))
    print(" +현재 수강 과목 ")
    for j in range(len(course_system_list[i].get('total_course_info').get('learning_course_info'))):
        print("   강의코드: "+course_system_list[i].get('total_course_info').get('learning_course_info')[j].get('course_code'))
        print("   강의 명: "+course_system_list[i].get('total_course_info').get('learning_course_info')[j].get('course_name'))
        print("   강사: "+course_system_list[i].get('total_course_info').get('learning_course_info')[j].get('teacher'))
        print("   개강일: "+course_system_list[i].get('total_course_info').get('learning_course_info')[j].get('open_date'))
        print("   종료일: "+course_system_list[i].get('total_course_info').get('learning_course_info')[j].get('close_date'))



str_start_menu ="""1. 학생 정보입력\n2. 학생 정보조회\n3. 학생 정보수정\n4. 학생 정보삭제\n5. 프로그램 종료\n메뉴를 선택하세요: """
str_read_menu ="""아래 메뉴를 선택하세요\n1. 전체 학생정보 조회\n--- 검색 조건 선택 ---\n2. ID검색\n3. 이름 검색\n4. 나이 검색\n5. 주소 검색\n6. 과거 수강 횟수 검색\n7. 현재 강의를 수강중인 학생\n8. 현재 수강중인 강의명\n9. 현재 수강 강사\n10. 이전 메뉴\n메뉴를 선택하세요: """
str_update_menu="1. 학생 이름\n2. 나이\n3. 주소\n4. 과거 수강 횟수\n5. 현재 수강 중인 강의 정보\n0. 이전 메뉴\n메뉴 번호를 입력하세요: "
str_update_munu_5="1. 강의 코드\n2. 강의명\n3. 강사\n4. 개강일\n5. 종료일\n0. 취소\n메뉴 번호를 입력하세요: "
str_delete_menu="삭제 유형을 선택하세요.\n1. 전체 삭제\n2. 현재 수강 중인 특정 과목정보 삭제\n3. 이전 메뉴\n메뉴 번호를 선택하세요: "
str_search="검색어를 입력하세요 :"


course_system_list=[]
std_dic={}
total_course_dic={}
learning_course_list=[]
id_count=0
index=[]
count=0
while True:
    print(''*20+'<<JSON기반 학생 정보 관리 프로그램 >>')
    sel_start_menu_num=int(input(str_start_menu))
    if sel_start_menu_num==5: #프로그램 종료
        break
    elif sel_start_menu_num==1:  #학생 정보 입력
        id_count+=1
        std_id='ITT'+str(id_count)
        std_name=input("이름 (예: 홍길동):")
        std_age=input("나이 (예: 29):")
        std_addr=input("주소 (예: 대구광역시 동구 아양로 135): ")
        num_of_learned_course=int(input("과거 수강 횟수 (예: 1): "))
        learning_course_yN=input("현재 수강 과목이 있습니까? (예: y/n): ")
        if learning_course_yN=='y' :
            fmore_learning_course()
        elif learning_course_yN=='n' :
            learning_course_list.append({})
        while True:
            anoter_leaning_course=input("현재 수강하는 과목이 더 있습니까? (y/n): ")
            if anoter_leaning_course=='y':
                fmore_learning_course()
            elif anoter_leaning_course=='n':
                break
        fput_std_dic()
        continue
    elif sel_start_menu_num==2: #학생 정보 조회
        sel_read_menu_num=int(input(str_read_menu))
        if sel_read_menu_num==10 :
            print()
            continue
        elif sel_read_menu_num==1 : #전체 학생정보 조회
            for i in range(len(course_system_list)):
                fread_std(i)
        elif sel_read_menu_num==2 : #id검색
            search_id=input(str_search)
            pass
        elif sel_read_menu_num==3 : #이름검색
            search_name=input(str_search)
            for i in range (len(course_system_list)):
                if search_name == course_system_list[i].get("student_name") :
                    index.append(i)
                    count+=1
                if count>=2 :
                    print("복수의 결과가 출력되었습니다.")
                fread_std(index)
        elif sel_read_menu_num==4 : #나이검색
            pass
        elif sel_read_menu_num==5 : #주소검색
            pass
        elif sel_read_menu_num==6 : #과거 수강횟수검색
            pass
        elif sel_read_menu_num==7 : #현재 강의 수강중인 학생 검색
            pass
        elif sel_read_menu_num==8 : #현재 운영중인 강의명
            pass
        elif sel_read_menu_num==9 : #현재 수업중인 강사
            pass
    elif sel_start_menu_num==3: # 학생 정보 변경
        update_std_num=input('수정할 학생 ID를 입력하세요: ')
        sel_update_menu_num=int(input(str_update_menu))
        if sel_update_menu_num==0:
            print()
            continue
        elif sel_update_menu_num==1: pass
        elif sel_update_menu_num==2: pass
        elif sel_update_menu_num==3: pass
        elif sel_update_menu_num==4: pass
        elif sel_update_menu_num==5: pass
    elif sel_start_menu_num==4: #학생 정보 삭제
        del_std_num=input("삭제할 학생ID를 입력하세요: ")
        sel_delete_menu_num=int(input(str_delete_menu))
        if sel_delete_menu_num==3:
            print()
            continue
        pass