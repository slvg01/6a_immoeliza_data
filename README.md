# Immoweb Scraper
Immoweb Scraper is a Python program designed for efficiently scraping information about houses and appartments that are for sale Immoweb. The tool offers a command-line interface, allowing users to select the amount of data they want to scrape and save the scraped information in various file formats.

## Installation
To install Immoweb Scraper, follow these steps:

Clone the repository to your local machine using the command:
```
git clone https://github.com/slvg01/immo-eliza-scraping-Qbicle.git
```
```
cd immo-eliza-scraping-Qbicle
```
Ensure that you have the required dependencies installed by executing:
```
pip install -r requirements.txt
```

## How to Use
```
python main.py
```
Follow the on-screen prompts to:

Select the amount of pages you want to Scrape. For each page all properties are scraped. Note that new real estate projects will be skipped because they contain separate links to available properties. These separate links are included in the scraped data.

## Output
| Variable name            | Content                                                               | Type    |
| ------------------------ | --------------------------------------------------------------------- | ------- |
| URL                      | URL to access the property                                            | string  |
| Property ID              | Unique Identifier of the property                                     | string  |
| Locality                 | Name of the city or village where the property is located             | string  |
| Postal code              | Postal code of the locality                                           | string  |
| Price (euro)             | Price in euro of the property                                         | integer |
| Energy class             | Energy class of the property from A to F                              | string  |
| Construction year        | Year the property was built                                           | integer |
| TOS : New Construction   | Flag for New construction. 1 for new, 0 for older                     | integer |
| TOS : Tenement building  | Flag for tenement building. 1 for yes, 0 for no                       | integer |
| Type of property         | Describes wether the property is a house or appartment                | string  |
| Subtype                  | More detailed classification of the property type                     | string  |
| Building conditon status | Flag for building condition. 1 for good, 0 for bad                    | integer |
| Building condition       | Description of the building condition                                 | string  |
| Furnished                | Flag for furnishing. 1 is furnished, 0 is not furnished               | integer |
| Living surface (sqm)     | Surface of the living area in square meters                           | integer |
| Nb of Bedrooms           | Number of bedrooms in the property                                    | integer |
| Kitchen equipped         | Flag for kitchen equipment. 1 is equipped, 0 is not equipped          | integer |
| Kitchen type             | Description of the kitchen equipment                                  | string  |
| Open fire                | Flag for open fire. 1 is present, 0 is absent                         | integer |
| Swimming pool            | Flag for swimming pool. 1 is present, 0 is absent                     | integer |
| Plot surface (sqm)       | Surface of the entire plot (garden + living surface) in square meters | integer |
| Terrace                  | Flag for terrace. 1 is present, 0 is absent                           | integer |
| Terrace surface (sqm)    | Surface of the terrace in square meters                               | integer |
| Garden                   | Flag for garden. 1 is present, 0 is absent                            | integer |
| Garden surface (sqm)     | Surface of the garden in square meters                                | integer |
| Number of frontages      | Number of frontages the property has                                  | integer |

## Contributors
[Mahak Behl](https://github.com/MahakBehl)
[Sylvain Legay](https://github.com/slvg01)
[Maarten Knaepen](https://github.com/MaartenKnaepen)


