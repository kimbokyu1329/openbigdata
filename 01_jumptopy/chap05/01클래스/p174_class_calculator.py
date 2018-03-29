class Calculator:
    def __init__(self):
        self.result=0
        self.via=[i for i in [1,2,3,4]]
    def adder(self,num):
        self.result +=num + self.via[3]

        return self.result

cal1=Calculator()
cal2=Calculator()

print(cal1.adder(1))
print(cal1.adder(4))

print(cal2.adder(6))
print(cal2.adder(4))

print(cal1.adder(2))