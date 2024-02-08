
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
import pandas as pd

class Immoweb_Scraper:
    """
    A class for scraping data from the Immoweb website.
    """

    def __init__(self) -> None:
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


        
    def get_base_urls(self):
        """
            Get the list of base URLs after applying the filter 
            as Life Annuity as False. Go through mupltiple pages 
            to get the list of all base URLs which will allow  
            fetching 10000 URLs of House or Appartment for sale.
        """
        for i in range(1,10):
            base_url = f"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&isALifeAnnuitySale=false&page={i}&orderBy=relevance"
            self.base_urls_list.append(base_url)
        print('Base URLs generated!')
        return(self.base_urls_list)    
    

        
    def get_immoweb_urls(self, session, url):
        """
        Gets the list of Immoweb URLs from each page of base URLs
        """
        with session.get(url) as url_content:
            self.base_urls_list = self.get_base_urls()
            counter = 0
            for each_url in self.base_urls_list:
                url_content = session.get(each_url).content
                soup = BeautifulSoup(url_content, "html.parser")
                for tag in soup.find_all("a", attrs={"class": "card__title-link"}):
                    immoweb_url = tag.get("href")
                    if "www.immoweb.be" in immoweb_url and counter < 100 and "new-real-estate-project" not in immoweb_url:
                        self.immoweb_urls_list.append(immoweb_url)
                        counter += 1
            self.immoweb_urls_list = list(dict.fromkeys(self.immoweb_urls_list))
            print('Immoweb URLs generated!', len(self.immoweb_urls_list))
            return self.immoweb_urls_list
      
       
    def scrape_table_dataset(self, url):
        """
        Get the 1st part of the parameters from URLs extracting
        and the 2nd part of the parameters from page scraping
        """
        with requests.Session() as session:
            self.immoweb_urls_list = self.get_immoweb_urls(session, url)
            with ThreadPoolExecutor() as executor:
                results = executor.map(self.process_url, self.immoweb_urls_list)
                for result in results:
                    self.data_set.append(result)
            return self.data_set

    def process_url(self, each_url):
        """
        Process each URL to scrape data.
        """
        data_dict = {}
        data_dict["url"] = each_url
        data_dict["Property ID"] = each_url.split('/')[-1]
        data_dict["Locality name"] = each_url.split('/')[-3]
        data_dict["Postal code"] = each_url.split('/')[-2]
        data_dict["Subtype of property"] = each_url.split('/')[-5]
        
        # Scraping logic
        with requests.Session() as session:
            url_content = session.get(each_url).content
        soup = BeautifulSoup(url_content, "html.parser")
        for tag in soup.find("div",attrs={"id" : "classified-description-content-text"}).find_all("p"):
            if "open haard" in tag.text.lower() or "cheminee" in tag.text.lower() or "feu ouvert" in tag.text.lower() or "open fire" in tag.text.lower():
                data_dict["Open Fire"] = 1
            else:
                data_dict["Open Fire"] = 0
        for tag in soup.find("p", attrs={"class": "classified__price"}):
            if tag.text.startswith("€"):
                data_dict["Price"] = tag.text[1:]
        for tag in soup.find_all("tr", attrs={"class": "classified-table__row"}):
            for tag1 in tag.find_all("th", attrs={"class": "classified-table__header"}):
                if tag1.string is not None:
                    for element in self.element_list:
                        if element == tag1.string.strip():
                            tag_text = str(tag.td).strip().replace("\n", "").replace(" ", "")
                            start_loc = tag_text.find('>')
                            end_loc = tag_text.find('<', tag_text.find('<') + 1)
                            table_data = tag_text[start_loc + 1:end_loc]
                            data_dict[element] = table_data
        
        return data_dict

    def update_database(self):
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
        print(self.data_set_df)
        return self.data_set_df     
         


    def to_csv (self):
        """ allow to convert the data_set DataFrame in CSV """
        data_set = self.data_set_df.to_csv ('data_set.csv', index= False)
        return data_set


        
url = "https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&isALifeAnnuitySale=false&page=1&orderBy=relevance"

# Example usage and testing:
immoscrap = Immoweb_Scraper()
#immoscrap.get_immoweb_urls()
#immoscrap.request_urls()
immoscrap.scrape_table_dataset(url)
immoscrap.update_database()
print(len(immoscrap.data_set))
#print(len(immoscrap.data_set))
#immoscrap.to_DataFrame()
#immoscrap.to_csv()
