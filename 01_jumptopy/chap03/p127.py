#coding: cp949

coffee=10
while True :
    money=int(input("\n���� ��������: "))

    if money==300:
        print("Ŀ�ǰ� ���ɴϴ�. ��ø� ��ٷ��ּ���.")
        coffee-=1
    
    elif money>300:
        print("Ŀ�ǰ� ���ɴϴ�. ��ø� ��ٷ��ּ���. \n�Ž����� {0}���� ��ȯ�˴ϴ�.".format(money -300))
        coffee-=1
    
    else:
        print("���� �����Ͽ� ��ȯ�˴ϴ�.")
    
    print("���� Ŀ���� ���� %d�� �Դϴ�."% coffee) #indentation while�� ���缭 �׻� Ŀ�Ǿ��� ��µǵ�����
    
    if not coffee:
        print("Ŀ�ǰ� �� ���������ϴ�. �ǸŸ� �����մϴ�.")
        break
    





