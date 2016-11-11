import requests
import re
from bs4 import BeautifulSoup

url = "http://www.bing.com/search?q=surgical+strike+by+india&qs=n&form=QBLH&pq=surgical+strike+by+india&sc=0-0&sp=-1&sk=&cvid=80AD441A646D44E09BBEF12212492590"

r = requests.get(url)

soup = BeautifulSoup(r.content,"lxml")
my_list = []

for link in soup.findAll('li',{'class' : 'b_algo'}):
    #print link.a['href']
    my_list.append(link.a['href'])

   

thefile = open('test.txt', 'w')


for item in my_list:
    thefile.write("%s\n\n" % item)
