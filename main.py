from scraper.scraper3 import Immoweb_Scraper
import time

def main():
      print('Welcome to Immoweb Scraper!\n'
            'Enter how many pages you want to scrape (max 333 pages)')
      numpages = int(input('Enter number of pages:  '))
      start = time.time()
      immoscrap = Immoweb_Scraper(numpages+ 1)
      immoscrap.scrape_table_dataset()
      immoscrap.Raw_DataFrame()
      immoscrap.to_csv_raw()
      immoscrap.Clean_DataFrame()
      immoscrap.to_csv_clean()
      end = time.time()
      print("Time Taken: {:.6f}s".format(end-start))
      exit('Thank you for using Immoweb Scraper!')
if __name__ == '__main__':
    main()
