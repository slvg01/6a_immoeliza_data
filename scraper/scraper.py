
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
import pandas as pd


class Immoweb_Scraper:
    """
    A class for scraping data from the Immoweb website.
    """

    def __init__(self, numpages) -> None:
        """
        Initialize the Immoweb_Scraper object.
        
        Args:
        - numpages (int): Number of pages to scrape.
        """
        self.base_urls_list = []
        self.immoweb_urls_list = []
        self.element_list = ["Construction year","Bedrooms","Living area","Kitchen type","Furnished","Terrace surface", 
                             "Surface of the plot","Garden surface","Number of frontages","Swimming pool","Building condition",
                             "Energy class"]
        self.data_set = []
        self.dataset_df = pd.DataFrame(columns=["url", "Property ID", "Locality name", "Postal code", 
                                                 "Subtype of property", "Open Fire", "Price"] + self.element_list)
        self.numpages = numpages
        self.session = requests.Session()
    def get_base_urls(self):
        """
        Get the list of base URLs after applying the filter.
        
        Returns:
        - list: List of base URLs.
        """
        for i in range(1,self.numpages):
            base_url_house = f"https://www.immoweb.be/en/search/house/for-sale?countries=BE&isALifeAnnuitySale=false&page={i}&orderBy=relevance"
            base_url_apartment = f"https://www.immoweb.be/en/search/apartment/for-sale?countries=BE&isALifeAnnuitySale=false&page={i}&orderBy=relevance"
            self.base_urls_list.append(base_url_house)
            self.base_urls_list.append(base_url_apartment)
        print(f'Number of Base URLs generated: {len(self.base_urls_list)}')
        return self.base_urls_list

    def get_immoweb_urls(self, session):
        """
        Gets the list of Immoweb URLs from each page of base URLs.
        
        Args:
        - session (requests.Session): Session object for making HTTP requests.
        
        Returns:
        - list: List of Immoweb URLs.
        """
        self.session = session
        self.base_urls_list = self.get_base_urls()
        for each_url in self.base_urls_list:
            url_content = session.get(each_url).content
            soup = BeautifulSoup(url_content, "lxml")
            for tag in soup.find_all("a", attrs={"class": "card__title-link"}):
                immoweb_url = tag.get("href")
                if "www.immoweb.be" in immoweb_url and "new-real-estate-project" not in immoweb_url:
                    self.immoweb_urls_list.append(immoweb_url)
        self.immoweb_urls_list = list(dict.fromkeys(self.immoweb_urls_list))
        print(f'Number of Immoweb URLs generated: {len(self.immoweb_urls_list)}')
        return self.immoweb_urls_list

    def scrape_table_dataset(self):
        """
        Scrape data from Immoweb URLs.
        
        Returns:
        - list: List of dictionaries containing scraped data.
        """
        with requests.Session() as self.session:
            self.immoweb_urls_list = self.get_immoweb_urls(self.session)
            with ThreadPoolExecutor(max_workers=18) as executor:
                print('Scraping in progress')
                results = executor.map(self.process_url, self.immoweb_urls_list)
                for result in results:
                    self.data_set.append(result)
            return self.data_set

    def process_url(self, each_url):
        """
        Process each URL to scrape data.
        
        Args:
        - each_url (str): URL to scrape.
        
        Returns:
        - dict: Dictionary containing scraped data.
        """
        data_dict = {}
        data_dict["url"] = each_url
        data_dict["Property ID"], data_dict["Locality name"], data_dict["Postal code"], data_dict["Subtype of property"] = each_url.split('/')[-1], each_url.split('/')[-3], each_url.split('/')[-2], each_url.split('/')[-5]
        print(each_url)
        # Scraping logic
        with requests.Session() as self.session:
            url_content = self.session.get(each_url).content
        soup = BeautifulSoup(url_content, "lxml")
        try:
            for tag in soup.find("div",attrs={"id" : "classified-description-content-text"}).find_all("p"):
                if any(keyword in tag.text.lower() for keyword in ["open haard", "cheminée", "feu ouvert", "open fire"]):
                    data_dict["Open Fire"] = 1
                else:
                    data_dict["Open Fire"] = 0
        except:
            data_dict["Open Fire"] = 0
            print("AttributeError: 'NoneType' object has no attribute 'find'")
        try:    
            for tag in soup.find("p", attrs={"class": "classified__price"}):
                if tag.text.startswith("€"):
                    data_dict["Price"] = tag.text.split(' ')[0][1:]
        except: 
            data_dict["Price"] = 0
            print("AttributeError: 'NoneType' object has no attribute 'find'")
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

    def update_dataset(self):
        """
        Missing information on webpage is populated as 0
        Example : If the information regarding swimming pool is not on webpage then
        in the dataset Swimming pull will be updated to 0
        """
        for each_dict in self.data_set:
            dict_elem = []
            for each_element in each_dict:
                dict_elem.append(each_element)
            for each_value in self.element_list:
                if each_value not in dict_elem:
                    each_dict[each_value] = 0
        return(self.data_set)

    def Raw_DataFrame(self):
        """ 
        Convert the data_set list of dict into a DataFrame 
        """
        self.data_set_df = pd.DataFrame(self.data_set)
        return self.data_set_df

    def to_csv_raw(self):
        """ 
        Convert the data_set DataFrame into CSV 
        """
        self.data_set_df.to_csv('data/raw_data/data_set_RAW.csv', index=False)
        print('A .csv file called "data_set_RAW.csv" has been generated. ')


    def Clean_DataFrame(self):
        """ 
            Allow to convert the data_set list of dict in a DataFrame 
            Allow to clean the DataFrame (inner aggregation, conversion, renaming )
        
        """
        self.data_set_df = self.Raw_DataFrame()
        self.data_set_df['Price'] = self.data_set_df['Price'].str.replace(',', '')
        col_to_conv = ['Price', 'Construction year','Number of frontages', 'Living area', 'Bedrooms', 'Terrace surface', 'Surface of the plot', 'Garden surface','Open Fire'] 
        for col in col_to_conv:
            if col in self.data_set_df.columns:
                self.data_set_df[col] = pd.to_numeric(self.data_set_df[col])
        col_to_none = ['Energy class','url','Property ID',	'Locality name','Postal code','Subtype of property', 'Open Fire','Price','Construction year', 'Subtype of property',  'Building condition','Furnished', 'Living area', 'Bedrooms', 'Kitchen type', 'Swimming pool', 'Surface of the plot', 'Terrace surface', 'Garden surface',	'Number of frontages']
        for col in col_to_none:
            if col in self.data_set_df.columns:
                self.data_set_df.loc[self.data_set_df[col] == 0, col] = 'None'
        self.data_set_df['TOS : New Construction'] = self.data_set_df['Construction year'].apply(lambda x: 'None'  if  x == 'None' else( 0 if x < 2023 else 1))
        self.data_set_df['TOS : Tenement building'] = self.data_set_df['Subtype of property'].apply(lambda x : 'None' if x == 'None' else (1 if x in ['mixed-use-building', 'apartment-block'] else 0))
        self.data_set_df['Type of property'] = self.data_set_df['Subtype of property'].apply(lambda x : 'None' if x == 'None' else ('Apartment' if x in ['apartment', 'loft', 'penthouse','duplex', 'ground-floor', 'flat-studio', 'service-flat'] else 'House'))
        self.data_set_df['Building conditon status'] = self.data_set_df['Building condition'].apply(lambda x : 'None' if x =='None' else ( 1 if x in ['Asnew', 'Good', 'Justrenovated'] else 0))
        self.data_set_df['Furnished'] = self.data_set_df['Furnished'].apply(lambda x : 'None' if x =='None' else (1 if x == 'yes' else 0))
        self.data_set_df['Kitchen equipped'] = self.data_set_df['Kitchen type'].apply(lambda x : 'None' if x =='None' else (0 if x == 'Notinstalled' else 1))
        self.data_set_df['Terrace'] = self.data_set_df['Terrace surface'].apply(lambda x : 0 if x == 'None' else ( 1 if x  > 0 else 0))
        self.data_set_df['Swimming pool'] = self.data_set_df['Swimming pool'].apply(lambda x : 'None' if x =='None' else (1 if x == 'yes' else 0))
        self.data_set_df['Garden'] = self.data_set_df['Garden surface'].apply(lambda x : 0 if x == 'None' else (1 if x  > 0 else 0))
        replace_dict1 = {'Asnew': 'As new', 'Justrenovated': 'Just renovated', 'Tobedoneup' : 'To be done', 'Torenovate':'To renovate'}
        replace_dict2 = {'Hyperequipped': 'Hyper equipped', 'Semiequipped': 'Semi equipped', 'USAhyperequipped' : 'USA hyper equipped', 'USAinstalled':'USA installed', 'Notinstalled' : 'Not installed'}
        self.data_set_df['Building condition'] = self.data_set_df['Building condition'].replace(replace_dict1)
        self.data_set_df['Kitchen type'] = self.data_set_df['Kitchen type'].replace(replace_dict2)
        self.data_set_df = self.data_set_df.rename(columns = {'url':'URL','Price': 'Price (euro)','Surface of the plot': 'Plot surface (sqm)','Open Fire' :'Open fire', 'Locality name':'Locality', 'Subtype of property': 'Subtype', 'Living area':'Living surface (sqm)', 'Bedrooms':'Nb of Bedrooms','Terrace surface': 'Terrace surface (sqm)','Garden surface':'Garden surface (sqm)'})
        new_col_order = ['URL','Property ID','Locality', 'Postal code', 'Price (euro)','Energy class','Construction year','TOS : New Construction', 'TOS : Tenement building', 'Type of property', 'Subtype','Building conditon status', 'Building condition', 'Furnished', 'Living surface (sqm)','Nb of Bedrooms','Kitchen equipped', 'Kitchen type','Open fire','Swimming pool','Plot surface (sqm)', 'Terrace','Terrace surface (sqm)','Garden', 'Garden surface (sqm)', 'Number of frontages']
        self.data_set_df = self.data_set_df[new_col_order]
        print(self.data_set_df.head(10))
        print('DataFrame is cleaned!')
        return self.data_set_df 

    def to_csv_clean(self):
        """ 
        Convert the data_set DataFrame into CSV 
        """
        self.data_set_df.to_csv('data/clean_data/data_set_CLEAN.csv', index=False)
        print('A .csv file called "data_set_CLEAN.csv" has been generated. ')

