import csv
import numpy

def num1_row(access_key):
    row_index = 0
    for i in range(len(data)):
        if data[i][0]==access_key :
            row_index=i
    row_instance=data[row_index]
    return row_instance
def num2_column(access_key):
    col_instance=[]
    col_index = data[0].index(access_key)
    for row in data[1:] :
        col_instance.append(row[col_index])
    return col_instance
def num3_sum(access_key) :
    return sum(typeChg(num2_column(access_key)))
def num4_avg(access_key) :
    return num3_sum(access_key)/len(num2_column(access_key))
def deviation(access_key):
    for i in range(len(num2_column(access_key))):
        print(num2_column(access_key)[i],"  \t\t\t",typeChg(num2_column(access_key))[i]-num4_avg(access_key))

def print_row(col_instance) :
    for row_element in col_instance:
        print(row_element)
def print_col(row_instance) :
    for col_element in row_instance:
        print(col_element,end=' ')
    print('')
def typeChg(col_instance) :
    try:
        col_instance_type_Chged=list(map(int,col_instance))
    except :
        col_instance_type_Chged=list(map(float,col_instance))
    return col_instance_type_Chged

with open("Demographic_Statistics_By_Zip_Code.csv",newline='') as infile :
    data = list(csv.reader(infile))
access_str="Access Key를 입력하세요: "

while True :
    sel_menu = int(input("0. 종료 1.행 2.열 3.총합 4.평균 5.최대값 6.최소값 7.편차 "
                         "8.표준편차 9.분산 10.오름차순 정렬 11.내림차순 정렬"
                         "\n메뉴를 선택하세요 : "))
    if sel_menu == 1: #행
        access_key = input(access_str)
        print("행 데이터는 다음과 같습니다")
        print_col(num1_row(access_key))
    elif sel_menu == 2: # 열
        access_key = input(access_str)
        print("열 데이터는 다음과 같습니다")
        print_row(num2_column(access_key))
    elif sel_menu == 3: # 총합
        access_key = input(access_str)
        print_row(num2_column(access_key))
        print("총합: ",num3_sum(access_key))

    elif sel_menu == 4: # 평균
        access_key = input(access_str)
        print_row(num2_column(access_key))
        print("평균: ",num4_avg(access_key))

    elif sel_menu == 5: # 최대값
        access_key = input(access_str)
        print_row(num2_column(access_key))
        print("최대값: ",max(typeChg(num2_column(access_key))))

    elif sel_menu == 6: # 최소값
        access_key = input(access_str)
        print_row(num2_column(access_key))
        print("최소값: ",min(typeChg(num2_column(access_key))))

    elif sel_menu == 7: #편차
        access_key = input(access_str)
        print("편차(Deviation) 공식 : 표본값 - 평균")
        print("표본  편차")
        deviation(access_key)
    elif sel_menu == 8: #표준편차
        access_key = input(access_str)
        print_row(num2_column(access_key))
        print("표준편차(Standard Deviation) 공식: √분산")
        print("표준편차: ",(numpy.var(typeChg(num2_column(access_key))))**0.5)

    elif sel_menu == 9: # 분산
        access_key = input(access_str)
        print_row(num2_column(access_key))
        print("분산(Variance) 공식: ∑(표본-평균)**2/표본수")
        print("분산: ",numpy.var(typeChg(num2_column(access_key))))

    elif sel_menu == 10: #오름차순
        access_key = input(access_str)
        order_list=typeChg(num2_column(access_key))
        order_list.sort()
        print_col(order_list)

    elif sel_menu == 11: #내림차순
        access_key = input(access_str)
        order_list=typeChg(num2_column(access_key))
        order_list.sort()
        order_list.reverse()
        print_col(order_list)

    else:
        print("프로그램을 종료합니다")
        break
    print('')
