from BeautifulSoup import BeautifulSoup
from multiprocessing import Pool
import os


def printToFile(a):
    if os.path.exists("D:\\Results\\Class 10\\10-36000\\34040-34500\\" + str(a) + ".html") == 1: 
         if os.path.getsize("D:\\Results\\Class 10\\10-36000\\34040-34500\\" + str(a) + ".html") >= 6990:
            print "exists"
            Index = 0
            TrIndex = 0
            f = open("D:\\Results\\Class 10\\10-36000\\34040-34500\\" + str(a) + ".html", "r")
            soup = BeautifulSoup(f)
            f.close()
            tables = soup.find('table')
            t = str(a)
            for table in tables:
                Index = Index + 1
                if Index == 6:
                    trs = table.find("tr")
                    for i in range(1,9):
                        trs = trs.nextSibling.nextSibling
                        td = trs.find("td")
                        t = t + " " + trs.find("td").text + " " + td.nextSibling.nextSibling.text + " " + td.nextSibling.nextSibling.nextSibling.nextSibling.text + " " + td.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text 

            with open("D:\\Parsed\\Class 10\\34040-34500.txt", "a") as text_file:
                text_file.write(t + '\n')

            

if __name__ == '__main__':
##       pool = Pool(processes=10)
##       pool.map(printToFile, range(34040,34500))
##       pool.close()
    printToFile(34499)
