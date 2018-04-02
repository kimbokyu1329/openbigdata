import os

print(os.getcwd())
os.chdir('..\\..\\..\\')
print(os.getcwd())

os.chdir('C:\\Windows')
print(os.getcwd())
os.system('dir > windows_file_list.txt')
os.system('notepad windows_file_list.txt') #fore그라운드로 시작되므로 이창을 닫아야지 밑에 코드가 실행이됨

f = os.popen('dir')
print(f.read())