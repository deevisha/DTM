from bs4 import BeautifulSoup
import urllib

f=open("pagelinks.txt","a+")
baseurl="http://www.bing.com/search?q=site%3Aeconomictimes.indiatimes.com+demonetization&qs=n&form=QBLH&sp=-1&pq=site%3Aec&sc=0-7&sk=&cvid=A935D5643BEE4D7EB355254C270C6898"
f.write("%s\n" %baseurl)
r = urllib.urlopen(baseurl).read()
soup = BeautifulSoup(r,"lxml")
all_links=soup.find_all("a")

lis=[]

for link in all_links:
	lis.append(link.get("href"))


for item in lis[41:45]:
	f.write("https://www.bing.com"+"%s\n" % item)
f.close()
