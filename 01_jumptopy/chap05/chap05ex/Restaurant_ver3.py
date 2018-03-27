class Restaurant :
    restaurent_name = 'NA'
    cuisine_type = 'NA'
    number_served=0
    def __init__(self,name,type):
        self.restaurent_name=name
        self.cuisine_type=type
    def describe_restaurant(self):
        print("저희 레스토랑의 명칭은 {0}이고 {1}전문점 입니다".format(self.restaurent_name,self.cuisine_type))
    def open_restauren(self):
        print("저희 {0} 레스토랑 오픈 했습니다. 어서오세요".format(self.restaurent_name))
    def reset_number_served(self):
        self.number_served=0
        print("손님 카운팅을 0으로 초기화 하였습니다.")
    def increment_number_served(self,number):
        self.number_served += number
    def check_customer_number(self):
        print("지금까지 총 {0}명의 손님께서 오셨습니다".format(self.number_served))

name,type = input("레스토랑의 이름과 요리 종류를 선택하세요(공백으로 구분) :").split()
rest=Restaurant(name,type)
rest.describe_restaurant()
openY_N=input("레스토랑을 오픈하시겠습니까? (y/n) :")
if openY_N =='y' :
    rest.open_restauren()
    while True :
        serving=input("어서 오세요 몇명 이십니까? (초기화:0입력, 종료:-1, 누적고객 확인:p) :")
        if str(serving) == 'p':
            rest.check_customer_number()
        elif int(serving) ==0:
            rest.reset_number_served()
        elif int(serving) == -1:
            break
        else :
            rest.increment_number_served(int(serving))
