import json
import re
import operator
with open('이명박_naver_news.json','r',encoding='utf8') as data_file:
    data = json.load(data_file)
null_count=0
count=0
domain_list=[]

for i in range (len(data)):
    if data[i]['org_link'] =='' :
        print('org_link가 없는 기사를 발견했습니다')
        null_count +=1
    else:
        p=re.compile("https?:\/\/([^:\/\?\s]+)")
        domain_list.extend(p.findall(data[i]['org_link']))
        count+=1
domain_list2=list(set(domain_list))
count_domain=len(domain_list2)
domain_counter = {}
for domain in domain_list :
    try : domain_counter[domain] +=1
    except : domain_counter[domain] =1
print(domain_counter)

print("<네이버 검색 빅데이터 분석>")
print("검색어: 이명박")
print('전체 도메인 수:',count_domain)
print("전체 건 수 :",count)
print("부정확한 데이터 수 :",null_count)
print("도메인 별 뉴스 기사 분석")

sorted_domain = sorted(domain_counter.items(),key=operator.itemgetter(1), reverse=True)
#sorted_domain = sorted(domain_counter,key=lambda k:k[1], reverse=True)
for i in range (len(sorted_domain)):
    print(sorted_domain[i])
