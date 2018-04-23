import urllib.request
import os
import math
from pandas import DataFrame

dir_name="V2_BigData"
dir_delimeter='\\'
nene_dir="Nene_Data"
nene_file='nene'
csv='csv'
record_limit=3

f=open('.\\nene_index.txt','r')
file_index=f.read()
file_index=int(file_index)+1
nene_dir_num=str(math.ceil(file_index/record_limit))
file_index=str(file_index)
f.close()
f=open('.\\nene_index.txt','w')
f.write(file_index)
f.close()


print("Start")
result = []
import xml.etree.ElementTree as ET
response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))
xml = response.read().decode('UTF-8')
root= ET.fromstring(xml)
print(root)
for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname5')
    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])
nene_table= DataFrame(result,columns=('store','sido','gungu','store_address'))

if not os.path.exists('.'+dir_delimeter+dir_name) :
    os.mkdir('.'+dir_delimeter+dir_name)
if not os.path.exists('.'+dir_delimeter+dir_name+dir_delimeter+nene_dir+nene_dir_num):
    os.mkdir('.'+dir_delimeter+dir_name+dir_delimeter+nene_dir+nene_dir_num)


nene_table.to_csv('.'+dir_delimeter+dir_name+dir_delimeter+nene_dir+nene_dir_num+dir_delimeter+nene_file+file_index+csv,encoding='utf8',mode='w',index=True)
print("End")
