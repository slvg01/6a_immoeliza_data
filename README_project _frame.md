# Immo Eliza - Data Collection

- Repository: `immo-eliza-scraping`
- Type: `Consolidation`
- Duration: `5 days`
- Deadline: `09/02/2023 3:00 PM` & presentations after
- Team: team (3-4 people)

## Learning Objectives

Use Python to collect as much data as possible.

At the end of this (sub)project, you will:
- Be able to scrape a website
- Be able to build a dataset from scratch
- Be able to collaborate in a team on a technical project

## The Mission

The real estate company "Immo Eliza" wants to develop a machine learning model to make price predictions on real estate sales in Belgium. They hired you to help with the entire pipeline.

Your first task is to build a dataset that gathers information about at least 10000 properties all over Belgium. This dataset will be used later to train your prediction model.

The final dataset should be a `csv` file with at least the following 18 columns:
- Property ID
- Locality name
- Postal code
- Price
- Type of property (house or apartment)
- Subtype of property (bungalow, chalet, mansion, ...)
- Type of sale (_note_: exclude life sales)
- Number of rooms
- Living area (area in m²)
- Equipped kitchen (0/1)
- Furnished (0/1)
- Open fire (0/1)
- Terrace (area in m² or null if no terrace)
- Garden (area in m² or null if no garden)
- Surface of good  
- Number of facades
- Swimming pool (0/1)
- State of building (new, to be renovated, ...)

## Must-have features (for the dataset)

- The data should have properties across all Belgium
- There should be at minimum unique 10000 data points
- Missing information is initially encoded with `None`
- Whenever possible, record only numerical values (for example, instead of defining whether the kitchen is equipped using `"Yes"` or `"No"`, use binary values instead)
- Use appropriate and consistent column names for your variables (those will be key to training and understanding your model later on)
- No duplicates
- No empty rows

## Tips

- Think first before you do!
  - What's your team name?
  - Team roles
  - Plan of attack
  - Task management (Trello, [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/quickstart-for-projects), ...)
  - Branching strategy
  - Code review
  - Data collection, merging, and versioning
  - ...
- Python packages that will come in very handy: `requests`, `BeautifulSoup`, and `pandas`
  - You can use other scraping tools such as `scrapy` but only if your entire team is comfortable with it!
  - Keep it light in terms of `pandas` tooling, we'll give you some time afterwards to dive deeper into it for the analysis and visualization part
- You can use concurrency to increase the speed of data collection
- You might have to work around CAPTCHA and other measures that want to slow you down in the scraping process - be creative ;-)
- Commit regularly and often - everyone should contribute equally based on the commit history

## Quality Assurance

Read our "Coding Best Practices Manifesto" and apply what's in there!

## Deliverables

1. Publish your source code on a GitHub repository:
    - Make a private repository first (`immo-eliza-scraping-teamname`), share it with your team and coaches
      - Make it public at the end of the project
    - Have a `scraper` folder with your Python modules for scraping
    - Have a `data` folder with the dataset - feel free to subdivide the folder (e.g. `raw`, `cleaned`)
    - Have a `README.md` file
    - Have a `main.py` file to run the scraper
    - Have a `requirements.txt` file
    - Have a `.gitignore` file

2. Write a convincing and clear README file, including following elements as you see fit:
   - Description
   - Installation
   - Usage
   - Sources
   - Visuals
   - Contributors
   - Timeline

3. Prepare a small presentation (of **15 minutes**):
   - How did you approach it?
   - What went wrong?
   - How did you solve issues?
   - What does the data look like?
   - What will be the next steps?

## Evaluation criteria

| Criteria       | Indicator                                  | Yes/No |
| -------------- | ------------------------------------------ | ------ |
| 1. Is complete | Contains a minimum of 10000 data points    |        |
|                | Contains data across whole Belgium         |        |
|                | The dataset has no empty rows              |        |
|                | There are few non-numeric values           |        |
|                | Your code is slick & clean                 |        |
|                | Repository and commit history is clear     |        |
| 2. Is great    | Used threading/multiprocessing             |        |

## Final note

_"Attempts to create thinking machines will be a great help in discovering how we think ourselves." - Alan Turing_

![You've got this!](https://i.giphy.com/media/JWuBH9rCO2uZuHBFpm/giphy.gif)
