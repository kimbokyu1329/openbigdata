import re

string='nene223.csv'
p=re.compile('(?<=[nene]).*(?=\.[csv])')
print(p.match(string))
