from BeautifulSoup import BeautifulSoup
import multiprocessing 

Index = 0
TrIndex = 0
f = open("D:\\Results\\Class9\\300000-350000\\300001.html", "r")
soup = BeautifulSoup(f)
f.close()
tables = soup.find('table')

for table in tables:
    Index = Index + 1
    if Index == 6:
        trs = table.find("tr")
        for i in range(1,8):
            trs = trs.nextSibling.nextSibling
            print trs.find("td").text
            td = trs.find("td")
            print td.nextSibling.nextSibling.text
            

