#coding: cp949

print("�ý� �ȳ� ���̵� ���α׷� ver2")

#money=2000
#print("������ ��� �ݾ��� �Է��ϼ��� : ",end='')
#money=int(input())

money=int(input("������ ��� �ݾ��� �Է��ϼ���: "))
#card=True
card=int(input("ī�带 �����ϰ� ��ʴϱ�? (1:�� 2:�ƴϿ�) : "))

print("\n���� ������ ��� �ݾ���" + str(money) + "�� �Դϴ�.")

if card==1:
    print("�ſ� ī�带 �����ϰ� ��ʴϴ�")
else:
    print("�ſ� ī�尡 �����ϴ�")


print("\n�м� ���")
if money >= 3000 or card ==1:
    print("�ýø� Ÿ�� ���� �� �ֽ��ϴ�.")
else:
    print("�ɾ� ���ž� �մϴ�.")

print("\n�ý� �ȳ� ���α׷��� �����մϴ�")
