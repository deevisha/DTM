import requests
import re
from bs4 import BeautifulSoup

f = open('pagelinks.txt', 'r')
fp = open('links.txt', 'w')

while 1:
	line=f.readline()
	if not line:
		break
	url = line

	r = requests.get(url)

	soup = BeautifulSoup(r.content,"lxml")
	my_list = []

	for link in soup.findAll('li',{'class' : 'b_algo'}):
		my_list.append(link.a['href'])

	for item in my_list:
		fp.write("%s\n" %item)
fp.close()
f.close()
