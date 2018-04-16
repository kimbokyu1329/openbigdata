class SuperRestaurant :
    # 속성
    type=''
    dessert='녹차'
    menu_list = []
    selnum=0
    # 행위
    def list(self):
        print('\n환영합니다. {0} 전문점 입니다. 메뉴를 선택하세요 :'.format(self.type))
        for i in range (0,len(self.menu_list)):
            print("{0}.{1}".format(i+1,self.menu_list[i]))
        self.selnum=int(input())-1
        print('{0}을 조리 중입니다. 잠시만 기다려주세요'.format(self.menu_list[self.selnum]))
    def serve(self):
        print('{0} 완성되었습니다. 맛있게 드세요 '.format(self.menu_list[self.selnum]))

    def dessert_serve(self):
        print('디저트 {0}가 서빙됩니다.'.format(self.dessert))

class Korean(SuperRestaurant):
    type='한식'
    menu_list = ['감자탕','갈비탕','돼지국밥','선지국','육개장','파전']

class Japaness(SuperRestaurant):
    type='일식'
    menu_list = ['모듬초밥','연어초밥','광어초밥','돈카츠','돈카츠 카레 우동','새우튀김 롤','우삼겹 우동전골']
class Western(SuperRestaurant):
    type ='양식'
    dessert ='커피'
    menu_list = ['비프 스테이크','스파게티','파스타','곤졸라 피자','아메리칸 브렉퍼스트','런치 샌드위치','샐러드']

while True :
    rest_type=int(input("식당을 선택하세요 (1. 한식 2. 일식 3. 양식) : "))
    if rest_type ==1 :
        A=Korean()
        A.list()
        A.serve()
        A.dessert_serve()
    elif rest_type ==2:
        B=Japaness()
        B.list()
        B.serve()
        B.dessert_serve()
    elif rest_type ==3:
        C=Western()
        C.list()
        C.serve()
        C.dessert_serve()
    else :
        break

