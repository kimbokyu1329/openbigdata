import urllib.request
import datetime
import json
import re

access_key="j5YUG1ECF3g15FFpfacOXDKVX61yfIehPuJGoIxCUmkhNQvhBz0NOGAuCGtjUIHfSuANH5Wt4VxT9tQ0ZGUsjQ%3D%3D"

def get_request_url(url):
    req=urllib.request.Request(url)

    try:
        response=urllib.request.urlopen(req)
        if response.getcode()==200:
            print("[%s] Url Request Success" %datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" %(datetime.datetime.now(),url))
        return None

def getNatVisitor(yyyymm,nat_cd,ed_cd):
    end_point='http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
    parameters="?_type=json&serviceKey=%s"%access_key
    parameters+="&YM="+yyyymm
    parameters+="&NAT_CD="+str(nat_cd)
    parameters+="&ED_CD="+str(ed_cd)
    url=end_point+parameters

    retData=get_request_url(url)
    if (retData==None):
        return None
    else:
        return json.loads(retData)

def main():

    with open('.\\national_code.txt','r',encoding='utf8') as infile :
        national_code_list=list(map(lambda x: x.rstrip().replace(' ',''), infile.readlines()))

    national_code_list[0]="000=미상"
    national_code_str=str(national_code_list)
    national_code_str=national_code_str[1:-1]
    national_code_str=national_code_str.replace('\'','').replace(',','').replace('=','')
    p=re.compile("(\d{3})([\w]*)\s")
    national_code_dic={}
    national_code_str_list=p.findall(national_code_str)
    for i in range(len(national_code_str_list)):
        national_code_dic[national_code_str_list[i][1]]=national_code_str_list[i][0]

    national_code_input=input("국가를 입력하세요: ")

    jsonResult=[]
    national_code=national_code_dic[national_code_input]
    ed_cd='E'
    print("기간을 입력하세요: ")
    nStartYearMonth=input('-시작 년/월 (ex : 201701): ')
    nEndYearMonth=input('-종료 년/월 (ex : 201712): ')

    nStartYear=int(nStartYearMonth[:4])
    nstartMonth=int(nStartYearMonth[4:])
    nEndYear=int(nEndYearMonth[:4])
    nEndMonth=int(nEndYearMonth[4:])


    for year in range(nStartYear,nEndYear):
        if year == nStartYear :
            for month in range(nstartMonth,13):
                yyyymm="{0}{1:0>2}".format(str(year),str(month))
                jsonData=getNatVisitor(yyyymm,national_code,ed_cd)

                if (jsonData['response']['header']['resultMsg']=='OK') :
                    krName= jsonData['response']['body']['items']['item']['natKorNm']
                    krName=krName.replace(' ','')
                    iTotalVisit=jsonData['response']['body']['items']['item']['num']
                    print('%s_%s:%s' %(krName,yyyymm,iTotalVisit))
                    jsonResult.append({'nat_name':krName,"nat_cd":national_code,'yyyymm':yyyymm,'visit_cnt':iTotalVisit})

        elif year ==nEndYear :
            for month in range(1,nEndMonth+1):
                yyyymm="{0}{1:0>2}".format(str(year),str(month))
                jsonData=getNatVisitor(yyyymm,national_code,ed_cd)

                if (jsonData['response']['header']['resultMsg']=='OK') :
                    krName= jsonData['response']['body']['items']['item']['natKorNm']
                    krName=krName.replace(' ','')
                    iTotalVisit=jsonData['response']['body']['items']['item']['num']
                    print('%s_%s:%s' %(krName,yyyymm,iTotalVisit))
                    jsonResult.append({'nat_name':krName,"nat_cd":national_code,'yyyymm':yyyymm,'visit_cnt':iTotalVisit})

        else :
            for month in range(1,13):
                yyyymm="{0}{1:0>2}".format(str(year),str(month))
                jsonData=getNatVisitor(yyyymm,national_code,ed_cd)

                if (jsonData['response']['header']['resultMsg']=='OK') :
                    krName= jsonData['response']['body']['items']['item']['natKorNm']
                    krName=krName.replace(' ','')
                    iTotalVisit=jsonData['response']['body']['items']['item']['num']
                    print('%s_%s:%s' %(krName,yyyymm,iTotalVisit))
                    jsonResult.append({'nat_name':krName,"nat_cd":national_code,'yyyymm':yyyymm,'visit_cnt':iTotalVisit})

    cnVisit=[]
    VisitYM=[]
    index=[]

    i=0
    for item in jsonResult:
        index.append(i)
        VisitYM.append(item['yyyymm'])
        cnVisit.append(item['visit_cnt'])

    with open('%s(%s)_해외방문객정보_%s_%s.json'%(krName,national_code,nStartYearMonth,nEndYearMonth),'w',encoding="utf8") as outfile:
        retJson = json.dumps(jsonResult,indent=4,sort_keys=True,ensure_ascii=False)
        outfile.write(retJson)

if __name__=='__main__':
    main()











