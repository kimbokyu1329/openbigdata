f=open("learning_python.txt","r")
line=f.readlines()
f.close()
#lines=list(map(lambda x: x.rstrip(),line))
for i in range(0,len(line)) :
    if i == 0 :
        f=open("learning_python.txt","w")
        line_str = str(line[i])
        line_str = line_str.replace('python','c')
        f.write(line_str)
        f.close()
    else :
        f=open("learning_python.txt","a")
        line_str = str(line[i])
        line_str = line_str.replace('python','c')
        f.write(line_str)
        f.close()



# f=open("learning_python.txt","r")
