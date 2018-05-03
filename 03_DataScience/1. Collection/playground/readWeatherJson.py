import json
with open ("기상예보.json",'r',encoding='utf8') as infile :
    jsonData=json.load(infile)

cateDic={}
with open ("카테고리밸류.txt",'r',encoding='utf8') as infile2 :
    categoryData=list(map(lambda x: x.strip(), infile2.readlines()))
    categoryData[0]='T1H'
for i in range(0,len(categoryData)-1,2):
    cateDic[categoryData[i]]=categoryData[i+1]
print(type(jsonData['fcstTime']))

# print(cateDic.items())

# for i in range (0,len(jsonData)):
#     print("예보 날짜",jsonData[i]['fcstDate'])
#     print("예보 시간",jsonData[i]['fcstTime'])
#     print("예보 종류",cateDic[jsonData[i]['category']])
#     print(jsonData[i]['fcstValue'])

