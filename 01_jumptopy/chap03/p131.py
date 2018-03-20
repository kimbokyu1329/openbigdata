#coding: cp949


student_name_lists=[
        ('김','보규'),
        ('문','희식'),
        ('이','효진'),
        ('문','창건')
        ]

#print(student_name_lists)
#for (last,first) in student_name_lists:
#    print(first+last)

#성을 입력받아 일치하는 이름을 출력하기

find=input("이름을 찾고자 하는 성을 입력하세요: ")
is_found_flag = False
for(last,first) in student_name_lists:
    if find == last:
        if is_found_flag ==False:
            print("<<검색결과>>")
            is_found_flag=True
        print(last+first)
