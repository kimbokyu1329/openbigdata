#coding: cp949
score_list=[]
i=0
number=0
print("<<�л� ���� �� ���α׷�>>")

while i!=5:
    score_list.append(int(input("{0}�� �л��� ������ �Է��ϼ���: ".format(i+1))))
    i+=1

print("*�򰡰��")
 
#for scoreList in score_list:
    
#    if scoreList > 60:
#        print(str(number)+"�� �л�" + str(score_list[number-1]) +"��, �հ��Դϴ�.")
#    else:
#        print(str(number)+"�� �л�" + str(score_list[number-1]) +"��, ���հ��Դϴ�.")
#    number+=1

for scoreList in score_list:
    number+=1    
    if scoreList > 60:
        print("{0}�� �л� {1}��, �հ��Դϴ�.".format(number,scoreList))
    else:
        continue #�ؿ����� ��� ���õǰ� �ٷ� for���� ó������ �� #number+=1 �� ���õ� 
        print("{0}�� �л� {1}��, ���հ��Դϴ�.".format(number,scoreList))
    number+=1    

