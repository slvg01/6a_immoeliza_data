from scraper.scraper import Immoweb_Scraper

print('Welcome to the Immoweb scraper by team Qbicle! \n'
      'to proceed, enter the number of pages you wish to scrape')
numpages = input('Number of pages is:  ')
print('Hold on, this can take a couple of minutes for a large amount of pages')
immoscrap = Immoweb_Scraper(numpages)
immoscrap.get_immoweb_urls()
immoscrap.request_urls()
if __name__ == "__main__":
    # Execute the main function if the script is run
    main()
