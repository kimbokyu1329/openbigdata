import sys
print("현재 Pycharm 에서 설정된 경로")
print(sys.path)

sys.path.append("C:\PythonMod\Mymodules")
print("현재 Pycharm 변경된 경로")
print(sys.path)

import mod3 #append 한후에 모듈을 추가해줘야됨

print(mod3.PI)
a=mod3.Math()
print(a.solv(2))
print(mod3.sum(mod3.PI,4.4)
