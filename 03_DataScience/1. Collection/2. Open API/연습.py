import re

with open('.\\national_code.txt', 'r', encoding='utf8') as infile:
    national_code_list = list(map(lambda x: x.rstrip().replace(' ', ''), infile.readlines()))

national_code_list[0] = "000=미상"
national_code_str = str(national_code_list)
# national_code_str = national_code_str[1:-1]
# national_code_str = national_code_str.replace('\'', '').replace(',', '').replace('=', '')
p = re.compile("[\[]?\'(\d{3})\=([\w]*)\'")
national_code_dic = {}
national_code_str_list = p.findall(national_code_str)
for i in range(len(national_code_str_list)):
    national_code_dic[national_code_str_list[i][1]] = national_code_str_list[i][0]

# for i in national_code_dic.items():
#     print(i)