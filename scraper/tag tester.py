from bs4 import BeautifulSoup
import requests 

urls = ['https://www.immoweb.be/en/classified/apartment/for-sale/zeebrugge/8380/11055156','https://www.immoweb.be/en/classified/apartment/for-sale/zeebrugge/8380/11088122']

soups = []


for url in urls:
    r = requests.get(url)
    print(url, r.status_code)
    soups.append(BeautifulSoup(r.content, "html.parser"))

title=[]
for soup in soups:
# - Get title
    for elem in soup.find("span", attrs={"class": "sr-only"}):
    # Just like that
        title.append(elem.text)

print(title)