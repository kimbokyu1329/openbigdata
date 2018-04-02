class Calculator:
    def __init__(self,list):
        self.list=list
        self.result = 0
    def sum(self):
        for i in range(0,len(self.list)) :
            self.result += self.list[i]
        return self.result
    def avg(self):
        return self.result/len(self.list)

if __name__ == '__main__':
    cal1=Calculator([1,2,3,4,5])
    print(cal1.sum())
    print(cal1.avg())


