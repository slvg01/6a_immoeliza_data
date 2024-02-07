from scraper.scraper import ImmowebScraper

if __name__ == "__main__":
    ImmowebScraper_object = ImmowebScraper()
    #base_urls = ImmowebScraper_object.get_base_urls()
    urls = ImmowebScraper_object.get_immoweb_urls()
    print(urls)

