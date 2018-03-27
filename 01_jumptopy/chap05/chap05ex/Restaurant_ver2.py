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
    def __del__(self):
        print("{0} 레스토랑 문닫습니다".format(self.restaurent_name))


rest_list=[]
for i in range(0,3):
    name,type = input("레스토랑의 이름과 요리 종류를 선택하세요(공백으로 구분) :").split()
    # rest=Restaurant(name,type)
    rest_list.append(Restaurant(name,type))
    rest_list[i].describe_restaurant()
    rest_list[i].open_restauren()

print("\n저녁 열시가 되었습니다\n")
#print(rest_list[0])
# rest_list[1].describe_restaurant()
# del rest