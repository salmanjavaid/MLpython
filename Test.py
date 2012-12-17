from BeautifulSoup import BeautifulSoup
from multiprocessing import Pool
import os

a = 300001

##for k in range(1,3):

def printToFile(a):    
    if os.path.getsize("D:\\Results\\Class9\\300000-350000\\" + str(a) + ".html") >= 6990:
        Index = 0
        TrIndex = 0
        f = open("D:\\Results\\Class9\\300000-350000\\" + str(a) + ".html", "r")
        
##        a = a + 1
        soup = BeautifulSoup(f)
        f.close()
        tables = soup.find('table')
        t = ""
        for table in tables:
            Index = Index + 1
            if Index == 6:
                trs = table.find("tr")
                for i in range(1,8):
                    trs = trs.nextSibling.nextSibling
                    td = trs.find("td")
                    t = t + trs.find("td").text + "  " + td.nextSibling.nextSibling.text + " "
        with open("D:\\Output.txt", "a") as text_file:
            text_file.write(t + '\n')

            

if __name__ == '__main__':
    pool = Pool(processes=10)
    pool.map(printToFile, range(300001, 350000))
