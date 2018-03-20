# f = open('foo.txt','w',encoding='UTF8')

# f.write("Life is too short, you need python")
with open('foo.txt','w',encoding='UTF8') as f :
    f.write("인생은 아름다워!")
#f.close
