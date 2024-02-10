import scrapy
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup
import pandas as pd
import time

class ImmowebSpider(scrapy.Spider):
    name = "immoweb"

    def __init__(self, numpages, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = self.get_base_urls(numpages)
        self.element_list = ["Construction year","Bedrooms","Living area","Kitchen type","Furnished","Terrace surface", 
                             "Surface of the plot","Garden surface","Number of frontages","Swimming pool","Building condition",
                             "Energy class"]
        self.data_set = []

    def get_base_urls(self, numpages):
        base_urls = []
        for i in range(1, numpages):
            base_urls.append(f"https://www.immoweb.be/en/search/house/for-sale?countries=BE&isALifeAnnuitySale=false&page={i}&orderBy=relevance")
            base_urls.append(f"https://www.immoweb.be/en/search/apartment/for-sale?countries=BE&isALifeAnnuitySale=false&page={i}&orderBy=relevance")
        self.logger.info(f'Number of Base URLs generated: {len(base_urls)}')
        return base_urls

    def parse(self, response):
        soup = BeautifulSoup(response.text, "lxml")
        for tag in soup.find_all("a", attrs={"class": "card__title-link"}):
            immoweb_url = tag.get("href")
            if "www.immoweb.be" in immoweb_url and "new-real-estate-project" not in immoweb_url:
                yield scrapy.Request(immoweb_url, callback=self.parse_immoweb)

    def parse_immoweb(self, response):
        data_dict = {}
        data_dict["url"] = response.url
        data_dict["Property ID"], data_dict["Locality name"], data_dict["Postal code"], data_dict["Subtype of property"] = response.url.split('/')[-1], response.url.split('/')[-3], response.url.split('/')[-2], response.url.split('/')[-5]

        try:
            open_fire = response.xpath('//div[@id="classified-description-content-text"]/p[contains(translate(text(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "open haard") or contains(translate(text(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "cheminée") or contains(translate(text(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "feu ouvert") or contains(translate(text(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "open fire")]/text()').get()
            data_dict["Open Fire"] = 1 if open_fire else 0
        except AttributeError:
            data_dict["Open Fire"] = 0

        price = response.css('p.classified__price::text').get()
        data_dict["Price"] = int(price.split(' ')[0][1:]) if price and price.startswith("€") else 0

        for tag in response.css("tr.classified-table__row"):
            th_text = tag.css("th.classified-table__header::text").get()
            if th_text and th_text.strip() in self.element_list:
                data_dict[th_text.strip()] = tag.css("td::text").get().strip().replace("\n", "").replace(" ", "")

        yield data_dict


class Immoweb_Scraper:

    def __init__(self, numpages):
        self.data_set = []
        self.numpages = numpages

    def scrape_data(self):
        process = CrawlerProcess(settings={
            'FEED_FORMAT': 'csv',
            'FEED_URI': 'data/raw_data/data_set_RAW.csv',
            'LOG_LEVEL': 'INFO'
        })
        process.crawl(ImmowebSpider, numpages=self.numpages)
        process.start()

    def to_csv_clean(self):
        """ 
        Convert the data_set DataFrame into CSV 
        """
        df = pd.DataFrame(self.data_set)
        # Clean dataframe and process it as before
        # ...
        df.to_csv('data/clean_data/data_set_CLEAN.csv', index=False)
        print('A .csv file called "data_set_CLEAN.csv" has been generated. ')

numpages = int(input('Enter number of pages: '))
start = time.time()
immoscrap = Immoweb_Scraper(numpages)
immoscrap.scrape_data()
immoscrap.to_csv_clean()
end = time.time()
print("Time Taken: {:.6f}s".format(end-start))
print(f'for {len(immoscrap.data_set)} rows on {immoscrap.numpages} scraped base urls')      
exit('Thank you for using Immoweb Scraper!')
