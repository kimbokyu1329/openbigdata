#coding: cp949
x=0
y=1
z=0

print("x:" + str(x) + " y:" +str(y)+" z:{0}".format(z)) #z를 출력할 수 있도록 포맷스트링으로 변경 
print("="*40)

if x or y :
    print(" x or y is true?")
    print("TRUE! if statement block 실행")
else :
    print(" x or y is true?")
    print("false 조건 불만족")
print("="*40)

if x and y :
    print(" x and y is true?")
    print("TRUE! if statement block 실행")
else :
    print(" x and y is true?")
    print("false 조건 불만족")
print("="*40)

if not x:
    print(" not x  is true? ")
    print("TRUE! if statement block 실행")
else :
    print(" not x is true? ")
    print("false 조건 불만족")
print("="*40)

if not y:
    print(" not y  is true? ")
    print("TRUE! if statement block 실행")
else :
    print(" not y  is true? ")
    print("false 조건 불만족")
print("="*40)

if x and y and z : 
    print("x and y and z : 조건 만족")
else :
    print("x and y and z : 조건 불만족")

if x or y or z :
    print("x or y or z : 조건 만족")
else :
    print("x or y or z : 조건 불만족")

print("="*40)
print("xyz , x+y+z 모두 참이 되도록 x y z 값을 재설정 하시오")
x=int(input("x :"))
y=int(input("y :"))
z=int(input("z :"))
print("="*40)
input_str="x:{0}, y:{1}, z:{2}".format(x,y,z)
print(input_str)
#print("x:{0}, y:{1}, z:{2}".format(x,y,z))

if x and y and z : 
    print("x and y and z : 조건 만족")
else :
    print("x and y and z : 조건 불만족")

if x or y or z :
    print("x or y or z : 조건 만족")
else :
    print("x or y or z : 조건 불만족")



