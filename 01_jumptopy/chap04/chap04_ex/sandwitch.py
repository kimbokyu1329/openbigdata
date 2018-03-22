ingredient_list=[]
ingredient=''
def input_ingredient(ingredient) :
    while True :
        ingredient = input("안녕하세요. 원하시는 재료를 입력하세요 : ")
        if ingredient=="종료" :
            break
        ingredient_list.append(ingredient)
    return ingredient_list
def make_sandwitch(ingrdient_list) :
    print("샌드위치를 만들고있습니다")
    for i in range (0,len(ingredient_list)):
        print("{0}를 추가합니다".format(ingredient_list[i]))
    print("주문 하신 샌드위치를 만들었습니다. 맛있게 드세요")

order=int(input(""""안녕하세요 저희 가게에 방문해 주셔서 감사합니다
1.주문
2.종료 """))

if order ==1 :
    input_ingredient(ingredient)
    print(ingredient_list)
    make_sandwitch(ingredient_list)