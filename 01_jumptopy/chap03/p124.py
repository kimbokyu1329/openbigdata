#coding: cp949

prompt="""
1.Add
2.Del
3.List
4.Quit

Enter number: """

number=0

while number!=4:
    number = int(input(prompt))
    if number==1:
        print("'Add' �޴��� �����ϼ̽��ϴ�")
    elif number==2:
        print("'Del' �޴��� �����ϼ̽��ϴ�")
    elif number==3:
        print("'List' �޴��� �����ϼ̽��ϴ�")
    elif number==4:
        print("���α׷��� ����˴ϴ�")
        break
    else:
        print("1~4 �޴��� �����˴ϴ�")
        
