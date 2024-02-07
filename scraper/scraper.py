
import csv
import requests
from bs4 import BeautifulSoup

variable_dict = {'ID':["div","class", "classified__header--immoweb-code"],
                 'Price': ["span", "class", "sr-only"]}


class Immoweb_Scraper:
    """
    A class for scraping data from the Immoweb website.
    """

    def __init__(self, variable_dict) -> None:
        """
        Initialize the Immoweb_Scraper object.

        Args:
        - variable_dict (dict): A dictionary containing variable names as keys and
                                corresponding CSS selectors as values.
        - urls (list): A list of URLs to scrape.
        """
        self.variable_dict = variable_dict
        self.base_urls_list = []
        self.soups = []
        
    def get_base_urls(self):
        for i in range(1,2):
            base_url = f"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&isALifeAnnuitySale=false&page={i}&orderBy=relevance"
            self.base_urls_list.append(base_url)
        print('Base URLs generated!')
        return(self.base_urls_list)    
        
    def get_immoweb_urls(self):
        self.immoweb_urls_list = []
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
        print('Immoweb URLs generated!', len(self.immoweb_urls_list))
        return(self.immoweb_urls_list)

    def request_urls(self):
        """
        Request URLs and parse HTML content.

        Sends HTTP requests to the provided URLs, parses the HTML content,
        and stores the parsed soup objects.
        """
        for url in self.immoweb_urls_list:
            r = requests.get(url)
            if r.status_code == 200:
                self.soups.append(BeautifulSoup(r.content, "html.parser"))
            else:
                continue
        print(len(self.soups))

    def scrape_vars(self):
        """
        Scrape data variables from parsed HTML content.

        Scrape data variables specified in the variable dictionary from
        the parsed HTML content and store them in lists.
        """
        self.listOfLists = [[] for _ in range(len(self.variable_dict))]
        for i, (k, v) in enumerate(self.variable_dict.items()):
            for soup in self.soups:
                if soup:
                    variable = soup.find(v[0], attrs={v[1]: v[2]})
                    if variable:
                        self.listOfLists[i].extend(elem for elem in variable)
                    else:
                        self.listOfLists[i].extend(None)
        print('Scraping successful')
        return self.listOfLists
    
    def get_elements_value(self):
        for soup in self.soups:
            for tag in soup.find_all("th", attrs={"class" : "classified-table__header"}):
                print(tag)
        print('Got elements')

    def to_dict(self):
        """
        Convert scraped data to a dictionary.

        Convert the scraped data lists to a dictionary where keys are
        variable names and values are corresponding lists.
        """
        self.immo_dict = dict(zip(self.variable_dict.keys(), self.listOfLists))
        print('Data was successfully converted to dictionary!')
        return self.immo_dict

    def save_csv(self):
        """
        Save scraped data dictionary to a CSV file.

        Save the scraped data dictionary to a CSV file where each key-value
        pair is written as a row with the key in the first column and the
        value in the second column.
        """
        with open('immo_dict.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in self.immo_dict.items():
                writer.writerow([key, value])

    def URL_extractor(self, url):
        """
        Extract data from URLs.

        Extract relevant data (IDs, Postal_codes, Locality_names, Subtypes)
        from the provided URLs.

        Args:
        - url (str): The URL from which data needs to be extracted.

        Returns:
        - dict: A dictionary containing extracted data.
        """
        splits = url.split('/')
        IDs = splits[-1]
        Postal_code = splits[-2]
        Locality_name = splits[-3].capitalize()
        Subtype = splits[-5]

        # Return the extracted data as a dictionary
        return {'ID': IDs, 'Postal_code': Postal_code, 'Locality_name': Locality_name, 'Subtype': Subtype}

    def extract_urls(self):
        """
        Extract data from URLs and save to a CSV file.

        Extract relevant data (IDs, Postal_codes, Locality_names, Subtypes)
        from the provided URLs, save the data to a dictionary, and then write
        the dictionary to a CSV file.
        """
        url_dict = {}

        IDs = []
        Postal_codes = []
        Locality_names = []
        Subtypes = []

        for url in self.urls:
            extracted_data = self.URL_extractor(url)
            IDs.append(extracted_data['ID'])
            Postal_codes.append(extracted_data['Postal_code'])
            Locality_names.append(extracted_data['Locality_name'])
            Subtypes.append(extracted_data['Subtype'])

        url_dict['IDs'] = IDs
        url_dict['Postal_codes'] = Postal_codes
        url_dict['Locality_names'] = Locality_names
        url_dict['Subtypes'] = Subtypes

        with open('url_dict.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in url_dict.items():
                writer.writerow([key, value])

        return url_dict
    
        

# Example usage and testing:
immoscrap = Immoweb_Scraper(variable_dict)
immoscrap.get_immoweb_urls()
immoscrap.request_urls()
#immoscrap.scrape_vars()
#immoscrap.to_dict()
#immoscrap.save_csv()
immoscrap.get_elements_value()
# immoscrap.extract_urls()




    

    

