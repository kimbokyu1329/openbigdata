import itertools
with open('.\\txtDir\\01','r') as file1:
    a=list(map(lambda x: x.rstrip().split() ,file1.readlines()))
    b=list(itertools.chain(*a))
    print(b)
