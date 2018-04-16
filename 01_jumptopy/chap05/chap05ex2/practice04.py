import sys

input_num1=int(input("세개의 양수를 입력하세요 (종료 :-1) :"))
if input_num1== -1 : sys.exit()
input_num2=int(input())
if input_num2== -1 : sys.exit()
input_num3=int(input())
if input_num3== -1 : sys.exit()

elif input_num3 % (input_num1*input_num2) ==0 :
    print("{0} 은 {1}와 {2}의 공배수 입니다".format(input_num3,input_num1,input_num2))
elif input_num3 % (input_num1*input_num2) !=0 :
    print("{0} 은 {1}와 {2}의 공배수가 아닙니다".format(input_num3,input_num1,input_num2))
