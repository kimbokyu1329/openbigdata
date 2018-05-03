import json
import urllib.request
from bs4 import BeautifulSoup
import re
import threading

g_Radiator = False
g_Gas_Valve = False
g_Balcony_Windows = False
g_Door = False
g_AI_Mode = False
g_humidifier = False
g_dehumidifier= False

def print_main_menu():
    print("\n1. 장비상태 확인")
    print("2. 장비제어")
    print("3. 스마트모드")
    print("4. 스마트모드 시뮬레이션")
    print("5. 검색")
    print("6. 프로그램 종료")

def print_device_status(device_name,devcie_status):
    print("%s 상태: "%device_name, end="")
    if devcie_status == True : print("작동")
    else: print("정지")

def check_device_status():
    print_device_status('난방기',g_Radiator)
    print_device_status('가스밸브', g_Gas_Valve)
    print_device_status('발코니(베란다) 창문', g_Balcony_Windows)
    print_device_status('출입문 상태', g_Door)
    print_device_status('가습기 상태', g_humidifier)
    print_device_status('제습기 상태', g_dehumidifier)

def print_device_menu():
    print("\n상태 변경할 기기를 선택하세요.")
    print("1. 난방기")
    print("2. 가스밸브")
    print("3. 발코니(베란다)창")
    print("4. 출입문")
    print("5. 가습기")
    print("6. 제습기")

def control_device():
    global g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door, g_humidifier, g_dehumidifier

    check_device_status()
    print_device_menu()
    menu_num = int(input("번호를 입력하세요: "))

    if menu_num == 1: g_Radiator = not g_Radiator
    if menu_num == 2: g_Gas_Valve = not g_Gas_Valve
    if menu_num == 3: g_Balcony_Windows = not g_Balcony_Windows
    if menu_num == 4: g_Door = not g_Door
    if menu_num == 5: g_humidifier = not g_humidifier
    if menu_num == 6: g_dehumidifier = not g_dehumidifier

    check_device_status()
def get_realtime_weather_info():
    print("자! 메뉴얼 보고 작성해 보세요!")

def smart_mode():
    global g_AI_Mode
    print("1. 인공지능 모드 조회")
    print("2. 인공지능 모드 상태 변경")
    print("3. 실시간 기상정보 Update")
    menu_num = int(input("메뉴를 선택하세요: "))

    if menu_num == 1:
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True: print("작동")
        else:print("중지")
    if menu_num == 2:
        g_AI_Mode = not g_AI_Mode
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True:
            print("작동")
            close_window()
        else: print("중지")

    elif menu_num == 3:
        get_realtime_weather_info()

def close_window(sim) :
    global g_Balcony_Windows, jsonData, jsonData_simul
    if sim == True :
        print("금일 {0}시 {1} 에 강수 {2}mm/h 가 확인되었습니다. \n창문이 자동으로 닫힙니다.".format(str(jsonData_simul['fcstTime'])[:2],str(jsonData_simul['fcstTime'])[2:],jsonData_simul['RN1']))
        g_Balcony_Windows = not g_Balcony_Windows
        return
    if g_Balcony_Windows ==True and jsonData['RN1'] >0 :
        print("금일 {0}시 {1} 에 강수 {2}mm/h 가 확인되었습니다. \n창문이 자동으로 닫힙니다.".format(str(jsonData['fcstTime'])[:2],str(jsonData['fcstTime'])[2:],jsonData['RN1']))
        g_Balcony_Windows = not g_Balcony_Windows
def hum(sim):
    global g_humidifier, jsonData, jsonData_simul
    if sim ==True :
        print("현재 습도가 낮습니다. (현재습도: {0}%%) \n가습기를 작동 시킵니다.".format(jsonData_simul['REH']))
        return
    if g_humidifier == False and jsonData['REH'] <30 :
        print("현재 습도가 낮습니다. (현재습도: {0}%%) \n가습기를 작동 시킵니다.".format(jsonData['REH']))
        g_humidifier = not g_humidifier
def dehum(sim):
    global  g_dehumidifier, jsonData,jsonData_simul
    if sim== True:
        print("현재 습도가 높습니다. (현재습도: {0}%) \n제습기를 작동 시킵니다.".format(jsonData_simul['REH']))
        return
    if g_dehumidifier ==False and jsonData['REH'] >= 70:
        print("현재 습도가 높습니다. (현재습도: {0}%) \n제습기를 작동 시킵니다.".format(jsonData_simul['REH']))
        g_dehumidifier = not g_dehumidifier




def Simulation_mode() :
    global g_AI_Mode ,jsonData,jsonData_simul
    prev=True
    print("스마트모드 시뮬레이션을 시작합니다. ".center(40,'='))
    if g_AI_Mode==False :
        print("> 스마트모드가 ON 되었습니다.")
        g_AI_Mode=True
        prev=False
    print("> 현재 기기의 상태")
    check_device_status()
    print("\n"+"-"*35)
    print("1. 비 오는날 ")
    print("2. 건조한 날 ")
    print("3. 습한 날 ")
    print("4. 이전")
    si_menu_num=int(input("시뮬레이션 할 메뉴를 선택하세요. :"))
    if si_menu_num==1 :
        jsonData_simul['RN1']=100
        close_window(1)
    elif si_menu_num==2 :
        jsonData_simul['REH']=10
        hum(1)
    elif si_menu_num ==3 :
        jsonData_simul['REH'] = 75
        dehum(1)
    g_AI_Mode=prev

def search():
    print("검색 메뉴를 선택하세요")
    print("1. 주변 맛집")
    print("2. 추천 드라마, 영화")
    print("3. 추천 기사(조회순)")
    search_num=int(input(">"))
    if search_num == 1 :
        location=input("맛집을 찾고자 하는 주소를 입력하세요 (예: 대구광역시 수성구 지산2동): ")
        location=location.replace(' ','')
        location=urllib.parse.quote(location)
        url2=urllib.parse.quote("맛집")
        url="https://store.naver.com/restaurants/list?filterId=r06140510&query={0}%20{1}".format(location,url2)
        # url="https://www.naver.com/"
        print(url)
        response=urllib.request.urlopen(url)
        bsData=str(BeautifulSoup(response.read().decode("UTF-8"),'html.parser'))
        p=re.compile("\"name\"\:\"([^\"]*)\"\,\"b")
        print(p.findall(bsData))
    elif search_num == 2 :
        url="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%B6%94%EC%B2%9C%EB%93%9C%EB%9D%BC%EB%A7%88&oquery=%EC%B6%94%EC%B2%9C%EB%93%9C%EB%9D%BC%EB%A7%88+%EC%98%81%ED%99%94&tqi=TXqVnspVuERsscB15HRssssssR4-047974"
        response=urllib.request.urlopen(url)
        bsData=str(BeautifulSoup(response.read().decode("utf8"),'html.parser'))
        p=re.compile("\<a[^\>]*[\>]([^\<]*)\<\/a\>\s\<\/strong\>")
        print(p.findall(bsData))
    elif search_num == 3 :
        url="http://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day"
        response=urllib.request.urlopen(url)
        bsData=str(response.read().decode("cp949"))
        p=re.compile("\<a[^\=]+\=\"([^\"]*)[^\>]+\>([^\<]+)\<\/a\>")
        print(p.findall(bsData))
with open ("기상예보.json",'r',encoding='utf8') as infile :
    jsonData=json.load(infile)
    jsonData_simul=jsonData
cateDic={}
with open ("카테고리밸류.txt",'r',encoding='utf8') as infile2 :
    categoryData=list(map(lambda x: x.strip(), infile2.readlines()))
    categoryData[0]='T1H'
for i in range(0,len(categoryData)-1,2):
    cateDic[categoryData[i]]=categoryData[i+1]

def scheduler() :
    threading.



print("<스마트 홈네트워크 시뮬레이션 프로그램 ver 1.0>")
print("                                 - 이현구 -")
while True:
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요: "))

    if(menu_num == 1):
        check_device_status()
    elif(menu_num ==2):
        control_device()
    elif(menu_num == 3):
        smart_mode()
    elif(menu_num == 4):
        Simulation_mode()
    elif(menu_num == 5):
        search()
    elif(menu_num == 6):
        break