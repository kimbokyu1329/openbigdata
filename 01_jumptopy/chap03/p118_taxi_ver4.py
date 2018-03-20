#coding: cp949

#pocket = ['paper','cellphone','money']
#pocket = ['card','money','paper','cellphone']
pocket=[]

item1=input("Pocket에 ITEM1을 챙기세요: ")
item2=input("Pocket에 ITEM2을 챙기세요: ")
item3=input("Pocket에 ITEM3을 챙기세요: ")
item4=input("Pocket에 ITEM4을 챙기세요: ")
item5=input("Pocket에 ITEM5을 챙기세요: ")
items=[item1,item2,item3,item4,item5]
pocket=items
print(pocket)

#item=input("item ?: ")
#pocket.append(item)


if 'card' in pocket : 
    print("카드로 택시를 탈 것을 추천합니다")

elif 'money' in pocket :
    print("현금 이용시 영수증을 꼭 챙기세요")
elif 'cellphone' in pocket:
    print("스마트폰에 교통카드 기능이 있는지 확인하시오")
else:
    pass # else를 나중에 추가 하고자 하더라도 pass 가 없으면 에러남 

