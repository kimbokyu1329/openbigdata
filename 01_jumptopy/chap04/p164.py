# f = open('G:\\python_workspace\\openbigdata\\01_jumptopy\\chap04\\새파일2.txt','r')
f = open('새파일2.txt','r')

lines = f.readlines()

for line in lines :
    print(line,end='')

f.close()
