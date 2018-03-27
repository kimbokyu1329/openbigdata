class SuperRestaurant :
    # 속성
    type=''
    dessert='녹차'
    menu_list = []
    # 행위
    def list(self):
        for i in range (0,len(self.menu_list)):
            print("{0}.{1}".format(i+1,self.menu_list[i]))
        print('\n환영합니다. {0} 전문점 입니다. 메뉴를 선택하세요 :'.format(self.type),end='')
    def cook(self,num):
        print('{0}을 조리 중입니다'.format(self.menu_list[num]))
        print('*:'*20)
        print('{0} 완성되었습니다. 맛있게 드세요 '.format(self.menu_list[num]))

    def dessert_serve(self):
        print('디저트 {0}가 서빙됩니다.'.format(self.dessert))

class Korean(SuperRestaurant):
    type='한식'
    seating = '마루'
    menu_list = ['감자탕','갈비탕','돼지국밥','선지국','육개장','파전']

class Japaness(SuperRestaurant):
    type='일식'
    main_ingredients='생선'
    menu_list = ['모듬초밥','연어초밥','광어초밥','돈카츠','돈카츠 카레 우동','새우튀김 롤','우삼겹 우동전골']
class Western(SuperRestaurant):
    type ='양식'
    dessert ='커피'
    menu_list = ['비프 스테이크','스파게티','파스타','곤졸라 피자','아메리칸 브렉퍼스트','런치 샌드위치','샐러드']

A=Korean()
B=Japaness()
C=Western()

A.list()
selnum=int(input())-1
A.cook(selnum)
A.dessert_serve()

B.list()
B.dessert_serve()

C.dessert_serve()
