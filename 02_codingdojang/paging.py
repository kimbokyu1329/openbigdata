#coding: cp949

string1='총건수(m): '
string2='한 페이지에 보여줄 게시물 수(n) (단 n은 1보다 크거나 같다. n >=1): '
m=int(input(string1))
n=int(input(string2))

page=m//n 
if m%n == 0:
    print(page)
elif m%n !=0:
    print(page + 1)
