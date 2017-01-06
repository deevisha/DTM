import urllib
from bs4 import BeautifulSoup
f=open("timesofindia.txt","r")
fp=open("a.txt","a")

while 1:
	line=f.readline()
	if not line:
		break
	url = line

# Opening a network object denoted by a URL for reading(suitable for series of url)
	uh = urllib.urlopen(url)
	print uh.getcode()# checking HTTP status code that was sent with the response
	data = uh.read()
	soup = BeautifulSoup(data,"lxml")

	g_data = soup.find_all("div",{"class":"Normal"})

	
	for item in g_data:
		fp.write("%s " % item.text.encode('cp850','replace').decode('cp850'))
		print(item.text.encode('cp850','replace').decode('cp850'))
	print "*"*50
	
fp.close()

f.close()