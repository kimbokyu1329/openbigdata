import urllib.request
from bs4 import BeautifulSoup
import csv
from pandas import DataFrame
rank=[num for num in range(51)]
name=[]
fluctuation=[]
fluctuation_num=[]

count=1
html = urllib.request.urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup=BeautifulSoup(html,'html.parser')
tbody = soup.tbody
tbody_html= BeautifulSoup(str(tbody),'html.parser')
tags_name=tbody_html.find_all('a')
tags_fluctuation=tbody_html.find_all('img')
tags_fluctuation_num=tbody_html.find_all('td',{'class':'range ac'})
for i in range (len(tags_name)) :
    for tag in tags_name[i].strings :
        name.append(tag)
for i in range (len(tags_fluctuation)) :
    if  count % 2 == 0:
        fluctuation.append(tags_fluctuation[i].attrs['alt'])
    count+=1
for i in range (len(tags_fluctuation_num)):
    for tag in tags_fluctuation_num[i].strings:
        fluctuation_num.append(tag)

print(rank)
print(name)
print(fluctuation)
print(fluctuation_num)
result=[]
fluc=[]
for i in range (50):
    fluc.append(fluctuation[i]+' '+fluctuation_num[i])
    result.append([rank[i]+1]+[name[i]]+[fluc[i]])
rank_table= DataFrame(result,columns=('순위','영화명','등락'))
print(rank_table)


rank_table.to_csv('naver_movie_rank',encoding='utf8',mode='w',index=False)
