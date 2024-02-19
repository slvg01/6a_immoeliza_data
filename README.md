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

## First Output = data_set_RAW


## Second output =  data_set_CLEAN
This first Output is cleaned and transform using a function called Clean_DataFrame() and lodge within the scraper.py script. 
Removes duplicate rows based on the 'Property ID'.
Filters out rows with incorrect postal codes (outside of belgium or mislabeled).
Replaces specific patterns in the 'Locality name' column to have the more readable.
Converts selected columns to numeric data type.
Classifies properties into 'Apartment' or 'House' based on the 'Subtype of property'.
Aggregates columns to create new features.
Determines the province and region based on the postal code.
Converts qualitative columns into boolean features.
Reformats text in specific columns for better readability.
Renames columns for clarity.
Reorders columns for better organization.

The final dataframe data_set_CLEAN has been adding the following columns under the following conditions :

| Variable name            | Content                                                               | Type    |
| ------------------------ | --------------------------------------------------------------------- | ------- |
| province                 | set the belonging province of the localit based on postal code         | string  |
| region                   | set the belonging region of the localit based on postal code               | string  |
| Type of property         | Describes whether the property is a house or appartment               | string  |
| New Construction Boolean | 1 if cnstruction year >= 2021, 0 for older                            | integer |
| Building cond. boolean   | 1 if good or just renovated, 0 for the rest                           | Integer |
| Energy class  boolean    | 1 for (B or better), 0 for the rest                                   | Integer |
| Double glazing boolean   | 1 if existing, 0 if not                                               | Integer |
| Elevator boolean         | 1 if existing, 0 if not                                               | Integer |
| Accessible boolean       | 1  if accessible for disabled people, 0 if not                        | Integer |
| Furnished boolean        | 1 is furnished, 0 is not furnished                                    | integer |
|Bathrooms total nb        | add bathroom and shower room colomn                                   | integer |
|Bathrooms total nb boolean| 1 is above 1 , 0 is below  rnished                                    | integer |
| Kitchen equipped         | 1 is equipped (sevral tag see code), 0 is not equipped                | integer |
| Open fire boolean        | Flag for open fire. 1 is present, 0 is absent                         | integer |
| Swimming pool boolean    | 1 is present, 0 is absent                                             | integer |
| Terrace boolean          |1 is present, 0 is absent                                              | integer |
| Garden  boolean          | 1 is present, 0 is absent                                             | integer |
| total parking            | add outddor and indoor parkig column numbers                          | integer |
| parking  boolean         | 1 is more 1 or more parking, 0 is absent                              | integer |
| Flood safe boolean       | 1 non flood zone , the rest is 0                                      | integer |
| Tenement building        | Flag for tenement building. 1 for yes, 0 for no                       | integer |

## Contributors
[Mahak Behl](https://github.com/MahakBehl)

[Sylvain Legay](https://github.com/slvg01)

[Maarten Knaepen](https://github.com/MaartenKnaepen)


## Code Visualization

![viz](https://github.com/slvg01/immo-eliza-scraping-Qbicle/blob/maarten/code%20viz.png)

This figure displays how the Immoweb Scraper function runs. The first method called is scrape_table_dataset. This method calls the function get_imoweb_urls which in turn calls get_base_urls.

get_base_urls loops through search result pages for both houses and appartments and creates URLs for up to 333 pages of search results each. These functions are then returned to get_immoweb_urls.

get_immoweb_urls creates a Session and then creates links for each property and returns those links to scrape_table_dataset.

scrape_table_dataset is where a ThreadPool is used. When this method gets the list of URLS. Then it concurrently applies the process_url method on each URL.

process_url is where the main scraping logic is implemented.

When all URLs are processed the Immoweb_Scraper object calls update_dataset to preprocess some data at the dataset level.

Then the output, a list of dictionaries, is converted to a DataFrame. The DataFrame is then saved using the to_csv_raw function or further processed by clean_dataframe and then saved in another location by the to_csv_clean function.

## Data set analysis and visualization

a whole data set visualization notebook can be found in the Analysis folder 
a presentation of the analysis of the dataframe can be seen in the Report folder 

