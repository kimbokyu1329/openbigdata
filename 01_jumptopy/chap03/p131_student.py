#coding: cp949
score_list=[]
i=0
number=0
print("<<학생 시험 평가 프로그램>>")

while i!=5:
    score_list.append(int(input("{0}번 학생의 점수를 입력하세요: ".format(i+1))))
    i+=1

print("*평가결과")
 
#for scoreList in score_list:
    
#    if scoreList > 60:
#        print(str(number)+"번 학생" + str(score_list[number-1]) +"점, 합격입니다.")
#    else:
#        print(str(number)+"번 학생" + str(score_list[number-1]) +"점, 불합격입니다.")
#    number+=1

for scoreList in score_list:
    number+=1    
    if scoreList > 60:
        print("{0}번 학생 {1}점, 합격입니다.".format(number,scoreList))
    else:
        continue #밑에줄은 모두 무시되고 바로 for문의 처음으로 감 #number+=1 도 무시됨 
        print("{0}번 학생 {1}점, 불합격입니다.".format(number,scoreList))
    number+=1    

