#coding: cp949

## 1
names_string='������,���翵,����ǥ,���翵,�ڹ�ȣ,������,���翵,������,�ֽ���,�̼���,�ڿ���,�ڹ�ȣ,������,����ȯ,���缺,������,������'
print('-'*30)
print('�达�� �̾��� ���� �� �� �ΰ���?')
print('�达�� ��:',names_string.count('��'))
print('�̾��� ��:',names_string.count('��'))
print('-'*30)
## 2
print('���翵"�̶� �̸��� �� �� �ݺ��ǳ���?: ',names_string.count('���翵'))
print('-'*30)

## 3 
names_list=names_string.split(',')
print('�ߺ����� ��')
print(names_list)
 
print('�ߺ����� ��')
names_set=set(names_list)
print(names_set)
print('-'*30)

## 4
names_list_new=list(names_set)
print(names_list_new)
names_list_new.sort()
#print(names_sorted)
print(names_list_new)


