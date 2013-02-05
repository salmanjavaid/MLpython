from BeautifulSoup import BeautifulSoup
from multiprocessing import Pool
import os

subjects = {}
location = "D:\\Results\\Class 10"
def printToFile(a):
     if os.path.exists(location + str(a) + ".html") == 1:
         if os.path.getsize(location + str(a) + ".html") >= 6990:
            Index = 0
            TrIndex = 0
            f = open(location + str(a) + ".html", "r")
            soup = BeautifulSoup(f)
            f.close()
            tables = soup.find('table')
            t = str(a)
            for table in tables:
                Index = Index + 1
                if Index == 6:
                    trs = table.find("tr")
                    for i in range(1,9):
                        try:
                            trs = trs.nextSibling.nextSibling
                            td = trs.find("td")
                            if subjects.has_key(td.text) == 0:
                                subjects[td.text] = td.text
                        except:
                            print "error file" + location + str(a) + ".html"
                            f = open('D:\\WrongFile.txt','a')
                            f.write("Format Error " + location + str(a) + ".html")
                            f.write('\n')
                            f.close()  
         else:
           print location + str(a) + ".html"
           f = open('D:\\WrongFile.txt','a')
           f.write("Size Error " + location + str(a) + ".html")
           f.write('\n')
           f.close()
    



def fileToParse():
   for dirname, dirnames, filenames in os.walk(loc):
     for filename in filenames:
        printToFile(os.path.join(dirname, filename))




if __name__ == '__main__':

   fileToParse()


   for subject in subjects:
        print subjects[subject]
   
