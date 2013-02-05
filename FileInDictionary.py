import os
from os.path import join, getsize
from BeautifulSoup import BeautifulSoup
loc = 'D:\\Results\\Class 10'
st = {}

for dirname, dirnames, filenames in os.walk(loc):
    for filename in filenames:
        print os.path.join(dirname, filename)
        
