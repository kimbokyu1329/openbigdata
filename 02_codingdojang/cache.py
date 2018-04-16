cache_size=int(input("캐쉬 사이즈를 입력하세요 :"))
city=input("도시를 입력하세요 (,로 구분) : ").split(',')
time=0
cache=[]
for i in range(0,cache_size):
    cache.append(city[i])
    time +=5
for i in range(cache_size,len(city)) :
    if city[i] in cache :
        time +=1
        del cache[0]
        cache.append(city[i])
    elif city[i] not in cache :
        time +=5
        del cache[0]
        cache.append(city[i])
print(time)