from BeautifulSoup import BeautifulSoup
import multiprocessing
import os

TrIndex = 0


Index = 0
f = open("D:\\Results\\Class 10\\10-36000\\34040-34500\\34495.html", "r")
print os.path.getsize("D:\\Results\\Class 10\\10-36000\\34040-34500\\" + "34495" + ".html")
soup = BeautifulSoup(f)
f.close()
tables = soup.find('table')
t = ""

for table in tables:
    Index = Index  + 1
    if Index == 6:
        trs = table.find("tr")
        for i in range(1,9):
            trs = trs.nextSibling.nextSibling
            print trs.find("td").text
            td = trs.find("td")
            t = t + " " + trs.find("td").text + " " + td.nextSibling.nextSibling.text + " " + td.nextSibling.nextSibling.nextSibling.nextSibling.text + " " + td.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text 


       

##with open("D:\\Parsed\\Class 10\\34040-34500 3.txt", "a") as text_file:
##            text_file.write(t)
