#coding: cp949

#pocket = ['paper','cellphone','money']
#pocket = ['card','money','paper','cellphone']
pocket=[]

item1=input("Pocket�� ITEM1�� ì�⼼��: ")
item2=input("Pocket�� ITEM2�� ì�⼼��: ")
item3=input("Pocket�� ITEM3�� ì�⼼��: ")
item4=input("Pocket�� ITEM4�� ì�⼼��: ")
item5=input("Pocket�� ITEM5�� ì�⼼��: ")
items=[item1,item2,item3,item4,item5]
pocket=items
print(pocket)

#item=input("item ?: ")
#pocket.append(item)


if 'card' in pocket : 
    print("ī��� �ýø� Ż ���� ��õ�մϴ�")

elif 'money' in pocket :
    print("���� �̿�� �������� �� ì�⼼��")
elif 'cellphone' in pocket:
    print("����Ʈ���� ����ī�� ����� �ִ��� Ȯ���Ͻÿ�")
else:
    pass # else�� ���߿� �߰� �ϰ��� �ϴ��� pass �� ������ ������ 

