def positive(x):
    return x>0

print(list(filter(positive,[1,-3,0,2,6])))

print(list(filter(lambda x:x>0,[1,2,3,0,-2,6])))