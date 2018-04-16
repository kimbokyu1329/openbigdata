import random
def cal(score,zone):
    return pow(score,zone_pow(zone))
def zone_pow(zone):
    if zone == 'S':
        return 1
    elif zone == 'D':
        return 2
    else :
        return 3

score=[]
zone=[]
zone_pool=['S','D','T']
option=[]
option_pool=['','*','#']
result=0
for i in range(3):
    score.append(random.randrange(1,4))
    zone.append(random.choice(zone_pool))
    option.append(random.choice(option_pool))
for i in range(3):
    if option[i] == '' :
        result+=cal(score[i],zone[i])
    elif option[i] == '*':
        result+=cal(score[i],zone[i])
        result= result*2
    else :
        result+=cal(score[i],zone[i])
        result= result*(-2)

print(score)
print(zone)
print(option)
print(result)