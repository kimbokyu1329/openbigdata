# f=open('.\\sample.txt','w')
#
# f.write('70\n')
# f.write('65\n')
# f.write('55\n')
# f.write('75\n')
# f.write('95\n')
# f.write('90\n')
# f.write('80\n')
# f.write('80\n')
# f.write('85\n')
# f.write('100')

#f.close()

d=open('.\\sample.txt','r')
lines=d.readlines()
print(lines)
d.close()

total=0
for line in lines:
    score = int(line)
    total += score
    print("s",score)
    print("t",total)

average = str(total / len(lines))

s=open('result.txt','w')
s.write(average)
s.close()
# while True:
#     lines=d.readline()
#     if not lines :
#         break
#     print(int(lines[:2]))

# lines2=d.read()
# lines2_list=list(lines2)
# print(lines2_list)