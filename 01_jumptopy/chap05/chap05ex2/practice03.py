print("-"*40)
print("10의 배수 확인 프로그램")
print("-"*40)

while True :
    input_num = int(input("양수를 입력하세요 (종료 : -1) :"))
    if input_num ==-1:
        break
    elif input_num % 10 ==0 :
        print("입력하신 {0}은 10의 배수 입니다\n".format(input_num))
    elif input_num % 10 !=0 :
        print("입력하신 {0}은 10의 배수가 아닙니다\n".format(input_num))
