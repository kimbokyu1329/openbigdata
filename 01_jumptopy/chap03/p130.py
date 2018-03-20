test_list=['one','two','three']
#for i in test_list:
#    print(i)

a=0
while True:
    i=test_list[a]
    a+=1
    print(i)
    if a>len(test_list)-1:
        break
