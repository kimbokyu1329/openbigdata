#coding: cp949

## 1
names_string='이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌'
print('-'*30)
print('김씨와 이씨는 각각 몇 명 인가요?')
print('김씨의 수:',names_string.count('김'))
print('이씨의 수:',names_string.count('이'))
print('-'*30)
## 2
print('이재영"이란 이름이 몇 번 반복되나요?: ',names_string.count('이재영'))
print('-'*30)

## 3 
names_list=names_string.split(',')
print('중복제거 전')
print(names_list)
 
print('중복제거 후')
names_set=set(names_list)
print(names_set)
print('-'*30)

## 4
names_list_new=list(names_set)
print(names_list_new)
names_list_new.sort()
#print(names_sorted)
print(names_list_new)


