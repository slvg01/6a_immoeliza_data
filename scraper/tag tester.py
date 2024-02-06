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
    table = soup.find('table', 'class' == 'classified-table')
    rows = table.find('tbody').find_all('tr')

    for row in rows:      
        header = row.find('th', class_='classified-table__header')
        if header and header.get_text == 'Construction year':
            # Extract value from corresponding table data cell
            construction_year = row.find('td', class_='classified-table__data')
            title.append(construction_year)
            break  # Stop iteration once the correct row is found

print(title)