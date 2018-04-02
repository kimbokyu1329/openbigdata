print(list(zip((1,2,3,4),(5,6,6,7))))

print(tuple('abc'))
print(list('abc'))

print(sorted([3,4,1,2,677,232],reverse=True))

a=[23,3,4,21,2]
result=a.sort()  # 리턴값이 없으므로 result에 할당되지않음 그러나 a 는 정렬은 된 상태

print(result)
result2=sorted(a)
print(result2)