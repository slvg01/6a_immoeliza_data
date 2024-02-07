import requests
from bs4 import BeautifulSoup
import re
from pprint import pprint

params = []
immoweb_urls_list = []


immoweb_urls_list = ['https://www.immoweb.be/en/classified/apartment-block/for-sale/forest/1190/11120343']

element_list = ["Bedrooms","Living area","Kitchen type","Furnished","Terrace surface","Garden surface","Number of frontages","Swimming pool","Building condition"]
el = 'Apartment block'
for each_url in immoweb_urls_list:
    url_content = requests.get(each_url).content
    soup = BeautifulSoup(url_content, "html.parser")
    print(each_url)
    for tag in soup.find_all("h1", attrs={"class" : "classified__title"}):
        print(tag.string.strip)
        tag_text = str(tag).strip().replace("\n","").replace(" ","")
        print(tag_text)
        if tag_text = 'ApartementBlokfor'
        
        
"""print(text)
        if tag : 
                param = tag.text.strip()
                params.append(param)
        else:
                params.append('N/A')
print(params)
    
    
   else:
        titles.append("Not found")
            
   if span_element:
        title = span_element.text.strip()
        titles.append(title)
    else:
        titles.append("Not found")         
            
            for element in element_list:
                #print(tag1.string.strip())
                if element == tag1.string.strip() :
                    tag_text = str(tag.td).strip().replace("\n","").replace(" ","")
                    #print(tag_text)
                    start_loc = tag_text.find('>')
                    end_loc = tag_text.find('<',tag_text.find('<')+1)
                    print(element + ' : '+ tag_text[start_loc+1:end_loc])
            
           
           
           
                
                
                    
open_fire = []

for immo_url in immoweb_urls_list:
    immo_content = requests.get(immo_url).content
    soup = BeautifulSoup(immo_content, "html.parser")
    for tag in soup.find("p" , attrs={"class" : "classified__description"}):
        if "open haard" in tag.text.lower() or "cheminee" in tag.text.lower() or "feu ouvert" in tag.text.lower() or "open fire" in tag.text.lower():
            


"""
"""for i in range(1,2):
    base_url = f"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&isALifeAnnuitySale=false&page={i}&orderBy=relevance"
    base_url_nopublicsale = f"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&isALifeAnnuitySale=false&isAPublicSale=false&page={i}&orderBy=relevance"
    base_urls_list.append(base_url)
    base_urls_list.append(base_url_nopublicsale)

counter = 0
for each_url in base_urls_list:
    url_content = requests.get(each_url).content
    soup = BeautifulSoup(url_content, "html.parser")
    for tag in soup.find_all("a", attrs={"class" : "card__title-link"}):
        immoweb_url = tag.get("href")
        if "www.immoweb.be" in immoweb_url and counter < 20:
            immoweb_urls_list.append(immoweb_url)
            counter += 1"""
