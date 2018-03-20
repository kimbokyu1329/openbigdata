list_first=[-1,1,3,-2,2]

list_negative=[]
list_positive=[]

for i in range (0,len(list_first)) :
    if list_first[i] < 0:
        list_negative.append(list_first[i])
    elif list_first[i] >=0:
        list_positive.append(list_first[i])
    list_result=list_negative+list_positive
print(list_result)





