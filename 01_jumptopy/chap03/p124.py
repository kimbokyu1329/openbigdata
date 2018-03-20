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
        print("'Add' 메뉴를 선택하셨습니다")
    elif number==2:
        print("'Del' 메뉴를 선택하셨습니다")
    elif number==3:
        print("'List' 메뉴를 선택하셨습니다")
    elif number==4:
        print("프로그램이 종료됩니다")
        break
    else:
        print("1~4 메뉴만 지원됩니다")
        
