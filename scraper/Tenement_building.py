import requests
from bs4 import BeautifulSoup


immoweb_urls_list = ['https://www.immoweb.be/en/classified/apartment-block/for-sale/forest/1190/11120343','https://www.immoweb.be/en/classified/mixed-use-building/for-sale/schaerbeek/1030/11122274']


for each_url in immoweb_urls_list:
    url_content = requests.get(each_url).content
    soup = BeautifulSoup(url_content, "html.parser")
    print(each_url)
    for tag in soup.find_all("h1", attrs={"class" : "classified__title"}):
        print(tag.string.strip)
        tag_text = str(tag).strip().replace("\n","").replace(" ","")
        print(tag_text)

