# Immoweb Scraper
Immoweb Scraper is a Python program designed for efficiently scraping information about houses and appartments that are for sale Immoweb. The tool offers a command-line interface, allowing users to select the amount of data they want to scrape and save the scraped information in various file formats.

## Installation
To install Immoweb Scraper, follow these steps:

Clone the repository to your local machine using the command:
```
git clone https://github.com/slvg01/immo-eliza-scraping-Qbicle.git
```
cd immo-eliza-scraping-Qbicle

Ensure that you have the required dependencies installed by executing:
```
pip install -r requirements.txt
```

## How to Use
```
python main.py
```
Follow the on-screen prompts to:

Select the amount of pages you want to Scrape. Per page 40 potential homes are scraped.

## Output
LeaderScraper provides the following features:

URL: The URL that was scraped, string

Property ID: The unique identifier of the property, string

Locality: The city or village where the property is located, string

Postal code: Postal code of the locality, string

TOS : New Construction

TOS : Tenement building

Type of property: either appartment or house, string

Subtype: subdivision of property type, string

Construction year: Year the property was built, integer

Building condition: Condition of the property, string

Furnished: 0 for not furnished, else 1

Living suface: amount of living surface in square meter, int

Nb of Bedrooms: Number of bedrooms, int

Equipped kitchen: 0 for not equipped, else 1

Plot Surface: Surface of the plot area in square meter, int

Terrace surface: Surface of the terrace in square meter, int

Garden surface: Surface of the garden in square meter, int

Number of frontages: Amount of frontages, int

## Contributors
[Mahak Behl](https://github.com/MahakBehl)
[Sylvain Legay](https://github.com/slvg01)
[Maarten Knaepen](https://github.com/MaartenKnaepen)


