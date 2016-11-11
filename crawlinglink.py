import requests
from bs4 import BeautifulSoup

url = "http://economictimes.indiatimes.com/news/defence/armys-daring-surgical-strike-marks-radical-change-in-indias-pakistan-policy/articleshow/54593808.cms"

r = requests.get(url)

soup = BeautifulSoup(r.content,"lxml")

g_data = soup.find_all("div",{"class":"Normal"})

for item in g_data:
	print(item.text.encode('cp850','replace').decode('cp850'))
