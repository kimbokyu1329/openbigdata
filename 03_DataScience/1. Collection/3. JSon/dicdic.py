a={'1':'adsfsadf'}
a['name']='pey'
print(a)
b=[a]
print(b)
c={'kk':'csadfsd','sdfa':{'cc':'sdfsdfsdfa'}}
b.append(c)
print(c.get('sdfa').get('cc'))