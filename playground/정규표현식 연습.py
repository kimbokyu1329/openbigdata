import re

string='nene223.csv'
p=re.compile('.*([0-9]*)(?=\.csv)')
print(p.match(string).group(2))
