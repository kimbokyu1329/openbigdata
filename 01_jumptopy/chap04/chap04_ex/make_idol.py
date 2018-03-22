f=open('연습생.txt','r',encoding='UTF8')
candidate_list=f.readlines()

def show_candidates():
     for i in range (0,len(candidate_list)):
          print(candidate_list[i].rstrip())
def make_idol():
     for i in range (0,len(candidate_list)):
          print("신예 아이돌 {0} 인기 급상승".format(candidate_list[i].rstrip()))
def make_world_star():
     for i in range (0,len(candidate_list)):
          print("아이돌 {0} 월드스타 등극".format(candidate_list[i].rstrip()))

show_candidates()
make_idol()
make_world_star()

f.close()
