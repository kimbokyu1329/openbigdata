import urllib.request
import json
import datetime
yyyymmdd=datetime.datetime.now().strftime('%Y%m%d')
timedelta=datetime.timedelta(minutes=40)
time=(datetime.datetime.now()-timedelta).strftime('%H%M')
req=urllib.request.Request('http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData?base_date={0}&base_time={1}&nx=89&ny=91&_type=json&ServiceKey=j5YUG1ECF3g15FFpfacOXDKVX61yfIehPuJGoIxCUmkhNQvhBz0NOGAuCGtjUIHfSuANH5Wt4VxT9tQ0ZGUsjQ%3D%3D&pageNo=1&numOfRows=30'
                           .format(yyyymmdd,time))
response=urllib.request.urlopen(req)
retData=response.read().decode('utf-8')
jsonData=json.loads(retData)
jsonResult=[]
jsonResultDic={}
w_item=jsonData['response']['body']['items']['item']
jsonResultDic['baseDate']=jsonData['response']['body']['items']['item'][0]['baseDate']
jsonResultDic['baseTime']=jsonData['response']['body']['items']['item'][0]['baseTime']
jsonResultDic['fcstDate']=jsonData['response']['body']['items']['item'][0]['fcstDate']
jsonResultDic['fcstTime']=jsonData['response']['body']['items']['item'][0]['fcstTime']
for i in range(0,len(jsonData['response']['body']['items']['item']),3) :
    if (jsonData['response']['body']['items']['item'][i]['category']=="RN1"
        or jsonData['response']['body']['items']['item'][i]['category']=="REH"
        or w_item[i]['category'] =="SKY"
        or w_item[i]['category'] =="PTY") :
            jsonResultDic[jsonData['response']['body']['items']['item'][i]['category']]=jsonData['response']['body']['items']['item'][i]['fcstValue']
    else : None


with open("기상예보.json",'w',encoding='utf8') as outfile :
    retJson=json.dumps(jsonResultDic,indent=4,sort_keys=True,ensure_ascii=False)
    outfile.write(retJson)

