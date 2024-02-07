import requests
from bs4 import BeautifulSoup

class ImmowebScraper:

    def __init__(self):
        self.base_urls_list = []
        self.immoweb_urls_list = []

    def get_base_urls(self):
        for i in range(1,2):
            base_url = f"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&isALifeAnnuitySale=false&page={i}&orderBy=relevance"
            self.base_urls_list.append(base_url)
        return(self.base_urls_list)
    
    def get_immoweb_urls(self):
        self.base_urls_list = self.get_base_urls()
        counter = 0
        for each_url in self.base_urls_list:
            url_content = requests.get(each_url).content
            soup = BeautifulSoup(url_content, "html.parser")
            for tag in soup.find_all("a", attrs={"class" : "card__title-link"}):
                immoweb_url = tag.get("href")
                if "www.immoweb.be" in immoweb_url and counter < 10:
                    self.immoweb_urls_list.append(immoweb_url)
                    counter += 1
        return(self.immoweb_urls_list)
    
    def get_elements_value(self):
        self.immoweb_urls_list = self.get_immoweb_urls()
        for each_url in self.immoweb_urls_list:
            url_content = requests.get(each_url).content
            soup = BeautifulSoup(url_content, "html.parser")
            for tag in soup.find_all("th", attrs={"class" : "classified-table__header"}):
                print(tag)
        
    

