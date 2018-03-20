# f = open('G:\\python_workspace\\openbigdata\\01_jumptopy\\chap04\\새파일2.txt','r')
f = open('새파일.txt','r',encoding='UTF8')

while True:
    line = f.readline()
    if not line :
        break
    print(line,end='')
f.close()