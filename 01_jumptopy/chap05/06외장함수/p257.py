import time

print(time.time())

print(time.localtime(time.time()))

my_time=time.localtime(time.time())
my_time.tm_year

print("안녕하세요. 현재 시각은 %d년 %d월 %d일 %d시 %d분 %d초 입니다" %(my_time.tm_year,my_time.tm_mon,my_time.tm_mday,
                                                    my_time.tm_hour,my_time.tm_min,my_time.tm_sec))
print(list(range(6)))
print(my_time[range(6)])

