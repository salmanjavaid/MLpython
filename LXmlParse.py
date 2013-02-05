from lxml import etree
from BeautifulSoup import BeautifulSoup


data = open('D:\\Results\\Class 10\\160000-180000\\160000.html','r').read()
doc = etree.HTML(data)
soup = BeautifulSoup(data)

count = 1
trs = soup.find('table')
print trs.find('tr')

##for tr1 in trs:
##  
##  if count == 6:
##    print tr1
## 
