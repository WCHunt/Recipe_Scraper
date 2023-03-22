# Recipe_Scraper

## Description
This script allows you to scrape recipe data from the Allrecipes website, including recipe titles, total time, ingredients, links, and images. The script uses the recipe_scrapers library to extract the data from individual recipe pages, and then iterates through multiple pages of recipes within a specified category. The resulting data is saved to a CSV file.

## Installation
Installation
To use this script, you will need to have Python 3 installed, as well as several Python packages. You can install the necessary packages by running the following 

command: pip install recipe-scrapers beautifulsoup4 pandas parse-ingredients requests

## Usage
To use the script, simply run the recipe_scraper.py file from the command line: python recipe_scraper.py.
The script will automatically scrape recipe data from the Allrecipes website and save it to a CSV file.

## Configuration
You can configure the script by modifying the mainCategories list at the beginning of the script. This list should contain URLs for the different recipe categories you want to scrape.

Additionally, you can modify the getPageData() function to extract different data from the recipe pages, or to scrape recipe data from different websites entirely.
