import urllib
from bs4 import BeautifulSoup as BS
from pandas import DataFrame
import csv
import os
import datetime
def make_dir():
    global dir_delimeter
    global dir_name
    os.mkdir('.'+dir_delimeter+dir_name)
def make_nene(dir_num):
    global dir_delimeter
    global dir_name
    global nene_dir
    os.mkdir('.'+dir_delimeter+dir_name+'\\'+nene_dir+dir_num)
def directory_num():
    global dir_delimeter
    global dir_name
    global nene_dir
    dir_num=len(os.listdir('.'+dir_delimeter+dir_name))
    while True:
        if len(os.listdir('.'+dir_delimeter+dir_name+dir_delimeter+nene_dir+str(dir_num))) == 3:
            dir_num+=1
            make_nene(str(dir_num))
        else : break
    return str(dir_num)
dir_name="V3_BigData"
dir_delimeter='\\'
nene_dir="Nene_Data"
nene_file=str(datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S'))
csv='csv'
record_limit=3

max_page=50
result=[]
index='index'
count=1

for page_idx in range(1,max_page+1):
    nene_url='https://nenechicken.com/17_new/sub_shop01.asp?page=%s&ex_select=1&ex_select2=&IndexSword=&GUBUN=A'%(str(page_idx))
    print(nene_url)
    response=urllib.request.urlopen(nene_url)
    soupData=BS(response.read().decode('UTF-8'),'html.parser')

    store_name=soupData.find_all('div',{'class':'shopName'})
    store_addr=soupData.find_all('div',{'class':'shopAdd'})
    store_phone=soupData.find_all('span',{'class':'tooltiptext'})
    for i in range(len(store_addr)):
        result.append([str(count)]+[store_name[i].text]+[store_addr[i].text]+[store_phone[i].text])
        count+=1
print(result)

nene_table=DataFrame(result,columns=('번호','지점명','주소','전화번호'))
nene_table.to_csv('.\\nene_지점_to_page50.csv',encoding='utf8',mode='w',index=False)

if not os.path.exists('.'+dir_delimeter+dir_name) :
    make_dir()
if not os.path.exists('.'+dir_delimeter+dir_name+dir_delimeter+nene_dir+'1'):
    make_nene('1')

nene_table.to_csv('.'+dir_delimeter+dir_name+dir_delimeter+nene_dir+directory_num()+dir_delimeter+nene_file+'.'+csv,encoding='utf8',mode='w',index=True)
print("End")