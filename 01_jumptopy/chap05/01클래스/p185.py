class Service:
    secret = "영구는 배꼽이 두개다"
    #name='NA'
    # def setname(self,name):
    #     self.name=name
    #     # return self.name
    def __init__(self,name):
        self.name=name
    def sum(self,a,b):
        result = a+ b
        print("%s님 %s + %s = %s 입니다"%(self.name,a,b,result))

# print(pey.secret)
# print(pey.setname("홍길동"))
# pey.sum(1,1)
pey=Service("홍길동")
pey.sum(1,3)

