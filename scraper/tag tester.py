from bs4 import BeautifulSoup
import requests 

urls = ['https://www.immoweb.be/en/classified/apartment/for-sale/zeebrugge/8380/11055156','https://www.immoweb.be/en/classified/apartment/for-sale/zeebrugge/8380/11088122']

soups = []
for url in urls:
    r = requests.get(url)
    print(url, r.status_code)
    soups.append(BeautifulSoup(r.content, "html.parser"))

titles = []
for soup in soups:
    # Get title
    elems = soup.find_all("span", attrs={"class": "overview__text"})
    for elem in elems:
        title_text = elem.get_text(strip=True)
        titles.append(title_text)

print(titles)