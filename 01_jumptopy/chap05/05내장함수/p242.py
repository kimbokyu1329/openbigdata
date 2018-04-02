sum = lambda a,b : a+b

print(sum(3,4))

myList = [lambda a,b : a+b ,lambda a,b:a*b] #myList[0] 하면 첫번째 함수에 접근가능

print(myList[0](3,4))