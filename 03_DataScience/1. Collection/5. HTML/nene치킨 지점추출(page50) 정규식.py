#정규식으로 원하는 데이터가 추출되는 것만 확인한 코드

import csv
from pandas import DataFrame
import re
import urllib
from bs4 import BeautifulSoup as BS

max_page=1
result=[]

for page_idx in range(1,max_page+1) :
    nene_url='https://nenechicken.com/17_new/sub_shop01.asp?page=%s&ex_select=1&ex_select2=&IndexSword=&GUBUN=A'%(str(page_idx))
    response=urllib.request.urlopen(nene_url)
    soupData=str(BS(response.read().decode('UTF-8'),'html.parser'))

    name=re.compile('\<div[^\>]*class\=[\'\"]?shopName[\'\"]?[\>]([^\<]*)\<\/div\>')
    print(name.findall(soupData))
    addr=re.compile('\<div[^\>]*class\=[\'\"]?shopAdd[\'\"]?[\>]([^\<]*)\<\/div\>')
    print(addr.findall(soupData))
    phone=re.compile('\<span[^\>]*class\=[\'\"]?tooltiptext[\'\"]?[\>]([^\<]*)\<\/span\>')
    # phone=re.compile('\<a[^\>]*href\=[\'\"]?(.*)[\"\']?\>')
    print(phone.findall(soupData))
