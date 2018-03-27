class Restaurant :
    restaurent_name = 'NA'
    cuisine_type = 'NA'
    def __init__(self,name,type):
        self.restaurent_name=name
        self.cuisine_type=type
    def describe_restaurant(self):
        print("저희 레스토랑의 명칭은 {0}이고 {1}전문점 입니다".format(self.restaurent_name,self.cuisine_type))
    def open_restauren(self):
        print("저희 {0} 레스토랑 오픈 했습니다. 어서오세요".format(self.restaurent_name))



name,type = input("레스토랑의 이름과 요리 종류를 선택하세요(공백으로 구분) :").split()

rest=Restaurant(name,type)
rest.describe_restaurant()
rest.open_restauren()