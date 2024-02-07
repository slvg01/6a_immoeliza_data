import timeit
import threading
from bs4 import BeautifulSoup
import requests
from requests.exceptions import SSLError
# Define your function here
def get_base_urls():
    base_urls_list = []
    for i in range(1,3):
        base_url = f"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&isALifeAnnuitySale=false&page={i}&orderBy=relevance"
        base_urls_list.append(base_url)
    print('Base URLs generated!')
    return base_urls_list


def get_immoweb_urls_session():
    immoweb_urls_list = []
    base_urls_list = get_base_urls()
    with requests.Session() as session:
        for each_url in base_urls_list:
            url_content = session.get(each_url).content
            soup = BeautifulSoup(url_content, "html.parser")
            for tag in soup.find_all("a", attrs={"class": "card__title-link"}):
                immoweb_url = tag.get("href")
                if "www.immoweb.be" in immoweb_url:
                    immoweb_urls_list.append(immoweb_url)

    print('Immoweb URLs generated!', len(immoweb_urls_list))
    return immoweb_urls_list

def request_urls_basic(immoweb_urls_list):
        """
        Request URLs and parse HTML content.

        Sends HTTP requests to the provided URLs, parses the HTML content,
        and stores the parsed soup objects.
        """
        soups=[]
        for url in immoweb_urls_list:
            r = requests.get(url)
            if r.status_code == 200:
                soups.append(BeautifulSoup(r.content, "html.parser"))
            else:
                continue
        print(len(soups))

def request_url(session, url):
    global soups
    with session.get(url) as response:
        if response.status_code == 200:
            html_content = response.content
            soup = BeautifulSoup(html_content, "html.parser")
            soups.append(soup)

def request_urls(urls):
    global soups
    with requests.Session() as session:
        threads = []
        for url in urls:
            thread = threading.Thread(target=request_url, args=(session, url))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

# Reset the soups list
soups = []

# Get the list of Immoweb URLs
a = get_immoweb_urls_session()

# Time the execution of the request_urls function
#execution_time = timeit.timeit(lambda: request_urls(a), number=1)
#print("Execution time:", execution_time, "seconds")

# Reset the soups list for the second execution
soups = []

# Time the execution of the request_urls function again
execution_time = timeit.timeit(lambda: request_urls(a), number=1)
print("Execution time:", execution_time, "seconds")

# Print the length of the soups list
print("Number of soups:", len(soups))