
import multiprocessing
import requests
from bs4 import BeautifulSoup
import pandas as pd
from requests.exceptions import SSLError
from concurrent.futures import ThreadPoolExecutor



class Immoweb_Scraper:
    """
    A class for scraping data from the Immoweb website.
    """

    def __init__(self, numpages) -> None:
        """
        Initialize the Immoweb_Scraper object.

        Args:
        - variable_dict (dict): A dictionary containing variable names as keys and
                                corresponding CSS selectors as values.
        - urls (list): A list of URLs to scrape.
        """
        self.base_urls_list = []
        self.immoweb_urls_list = []
        self.element_list = ["Construction year","Bedrooms","Living area","Kitchen type","Furnished","Terrace surface", "Surface of the plot","Garden surface","Number of frontages","Swimming pool","Building condition"]
        self.data_set = []
        self.dataset_df = pd.DataFrame()
        self.soups = []
        self.workers = int(multiprocessing.cpu_count() * 0.8)
        self.numpages = numpages
        self.session = requests.Session()


        
    def get_base_urls(self):
        """
            Get the list of base URLs after applying the filter 
            as Life Annuity as False. Go through mupltiple pages 
            to get the list of all base URLs which will allow  
            fetching 10000 URLs of House or Appartment for sale.
        """
        base_urls_list = []
        for i in range(self.numpages):
            base_url = f"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&isALifeAnnuitySale=false&page={i}&orderBy=relevance"
            base_urls_list.append(base_url)
        print('Base URLs generated!')
        return base_urls_list 
    

        
    def get_immoweb_urls_session(self):
        self.immoweb_urls_list = []
        self.base_urls_list = self.get_base_urls()
        with requests.Session() as session:
            for each_url in self.base_urls_list:
                url_content = session.get(each_url).content
                soup = BeautifulSoup(url_content, "html.parser")
                for tag in soup.find_all("a", attrs={"class": "card__title-link"}):
                    immoweb_url = tag.get("href")
                    if "www.immoweb.be" in immoweb_url and "new-real-estate-project" not in immoweb_url:
                        self.immoweb_urls_list.append(immoweb_url)
        self.immoweb_urls_list = list(dict.fromkeys(self.immoweb_urls_list))
        print('Immoweb URLs generated!', len(self.immoweb_urls_list))
        return self.immoweb_urls_list
    


    def request_url(self, session, url):
        """
        Request URLs and parse HTML content.

        Sends HTTP requests to the provided URLs, parses the HTML content,
        and stores the parsed soup objects.
        """
        try:
            with session.get(url) as response:
                if response.status_code == 200:
                    html_content = response.content
                    soup = BeautifulSoup(html_content, "lxml")
                    self.soups.append(soup)
        except SSLError as e:
            print(f"SSL Error occurred. Error: {e}")

    def request_urls(self): 
        self.session 
        urls = self.get_immoweb_urls_session()
        global soups
        self.soups = []  
        with ThreadPoolExecutor(max_workers=self.workers) as executor:
            #time.sleep(1)
            results = executor.map(lambda url: self.request_url(self.session, url), urls)
        print("Number of soups:", len(self.soups))
        return self.soups
       
    """def create_scraping_dict(self):
        self.scraping_dict = dict(zip(self.immoweb_urls_list, self.soups))  
        print('Scraping dict created!')
        return self.scraping_dict
    """

    def scrape_table_dataset(self):
        """  
            Get the 1st part of the parameters from URLs extracting
            and the 2nd part of the parameters from page scraping
        """
        
        self.immoweb_urls_list = self.get_immoweb_urls_session()
        for each_url in self.immoweb_urls_list:
            data_dict = {}
            data_dict["url"] = each_url
            data_dict["Property ID"] = each_url.split('/')[-1]
            data_dict["Locality name"] = each_url.split('/')[-3]
            data_dict["Postal code"] = each_url.split('/')[-2]
            data_dict["Subtype of property"] = each_url.split('/')[-5]
            #url_content = requests.get(each_url).content
        self.soups = self.request_urls()
        for soup in self.soups:
            #print(each_url)
            #for tag in soup.find("p" , attrs={"class" : "classified__description"}):
                #if "open haard" in tag.text.lower() or "cheminee" in tag.text.lower() or "feu ouvert" in tag.text.lower() or "open fire" in tag.text.lower():
                    #data_dict["Open Fire"] = 1
                #else:
                    #data_dict["Open Fire"] = 0
            for tag in soup.find("p" , attrs={"class" : "classified__price"}):
                    if tag.text.startswith("€"):
                        data_dict["Price"] = tag.text[1:]
            for tag in soup.find_all("tr", attrs={"class" : "classified-table__row"}):
                for tag1 in tag.find_all("th", attrs={"class" : "classified-table__header"}):
                    if tag1.string is not None:                
                        #print(tag1.string.strip())
                        for element in self.element_list:
                            if element == tag1.string.strip():
                                tag_text = str(tag.td).strip().replace("\n","").replace(" ","")
                                #print(tag_text)
                                start_loc = tag_text.find('>')
                                end_loc = tag_text.find('<',tag_text.find('<')+1)
                                table_data = tag_text[start_loc+1:end_loc]
                                #print(element + ' : '+ table_data)
                                data_dict[element] = table_data
            #print(data_dict)
            self.data_set.append(data_dict)
        return(self.data_set)

    def update_dataset(self):
        for each_dict in self.data_set:
            dict_elem = []
            for each_element in each_dict:
                dict_elem.append(each_element)  
                print(dict_elem)
            for each_value in self.element_list:
                if each_value not in dict_elem:
                    each_dict[each_value] = 0
        print(self.data_set)
        return(self.data_set)

    def to_DataFrame (self) :
        """ allow to convert the data_set list of dict in a DataFrame """
        self.data_set_df = pd.DataFrame(self.data_set)
        print(self.data_set_df.head(3))
        return self.data_set_df     
         


    def to_csv (self):
        """ allow to convert the data_set DataFrame in CSV """
        data_set = self.data_set_df.to_csv ('data_set.csv', index= False)
        return data_set


        

# Example usage and testing:
immoscrap = Immoweb_Scraper(1)
#immoscrap.request_urls()
#print(immoscrap.soups[1])
#immoscrap.create_scraping_dict()
#immoscrap.scrape_vars()
#immoscrap.to_dict()
#immoscrap.save_csv()
#immoscrap.get_elements_value()
scraped_data = immoscrap.scrape_table_dataset()
#scraped_data = immoscrap.scrape_table_dataset()
immoscrap.update_dataset()

print(scraped_data)
# immoscrap.extract_urls()