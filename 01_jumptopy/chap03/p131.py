#coding: cp949


student_name_lists=[
        ('��','����'),
        ('��','���'),
        ('��','ȿ��'),
        ('��','â��')
        ]

#print(student_name_lists)
#for (last,first) in student_name_lists:
#    print(first+last)

#���� �Է¹޾� ��ġ�ϴ� �̸��� ����ϱ�

find=input("�̸��� ã���� �ϴ� ���� �Է��ϼ���: ")
is_found_flag = False
for(last,first) in student_name_lists:
    if find == last:
        if is_found_flag ==False:
            print("<<�˻����>>")
            is_found_flag=True
        print(last+first)
