
from recipe_scrapers import scrape_me
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from parse_ingredients import parse_ingredient
import pandas as pd
import os
from datetime import datetime


def getPageData(page, firstPage=False):
    # Get the HTML content of the page and parse it with BeautifulSoup
    response = session.get(page)
    soup = BeautifulSoup(response.content, 'lxml')
    
    # Find all the recipe links on the page
    if firstPage:
        recipe_links = soup.find_all('a', class_="card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom")
    else:
        recipe_links = soup.find_all('a', class_="tout__titleLink elementFont__toutLink")
    
    # For each recipe link, extract information about the recipe
    for link in recipe_links:
        if re.search('\/recipe\/', link.get('href')):
            # Use recipe_scrapers library to extract title, total time, ingredients, and image of recipe
            scraper = scrape_me(link.get('href'))
            if link.get('href') not in link:
                # Parse the ingredients with the parse_ingredient function and extract the ingredient names
                title.append(scraper.title())
                time.append(scraper.total_time())
                betteringredient = [parse_ingredient(k).name for k in scraper.ingredients()]
                ingredients.append(betteringredient)
                image.append(scraper.image())
            # Add the link to the list of recipe links
            link.append(link.get('href'))


# define a main function to scrape recipes
def main():
    # define main categories
    mainCategories = ['https://www.allrecipes.com/recipes/17562/dinner/',
                      'https://www.allrecipes.com/recipes/78/breakfast-and-brunch/',
                      'https://www.allrecipes.com/recipes/17561/lunch/',
                      'https://www.allrecipes.com/recipes/76/appetizers-and-snacks/',
                      'https://www.allrecipes.com/recipes/156/bread/',
                      'https://www.allrecipes.com/recipes/79/desserts/',
                      'https://www.allrecipes.com/recipes/77/drinks/',
                      'https://www.allrecipes.com/recipes/80/main-dish/',
                      'https://www.allrecipes.com/recipes/96/salad/',
                      'https://www.allrecipes.com/recipes/81/side-dish/',
                      'https://www.allrecipes.com/recipes/94/soups-stews-and-chili/']
    
    # get current date and time and create output file name
    now = datetime.now()
    output_file_name = now.strftime("%Y-%m-%d_%H-%M-%S_recipes.csv")
    # create output path using the current working directory and output file name
    output_path = os.path.join(os.getcwd(), output_file_name)

    # define empty lists for recipe attributes
    title = []
    time = []
    link = []
    ingredients = []
    image = []

    # iterate through main categories and get recipe links on the first page
    for k in mainCategories:
        getPageData(k, firstPage=True)
        # create a dictionary of recipe attributes and store them in a pandas dataframe
        recipe_dict = {'Title': title, 'Time': time, 'Ingredients': ingredients, 'Link': link, 'Image': image}
        data_frame = pd.DataFrame(recipe_dict)
        # write the dataframe to a csv file
        data_frame.to_csv(output_path, 'w')

    # iterate through main categories and get recipe links on subsequent pages
    count = 2
    for j in mainCategories:
        # generate new page url by adding the page number to the original category url
        newpage = j + '?page=' + str(count)
        response = requests.get(str(newpage))
        # while the page returns a status code of 200, get recipe links
        while response.status_code != 400:
            # get recipe links and increment page count
            getPageData(newpage)
            count += 1
            # generate new page url with updated page number
            newpage = j + '?page=' + str(count)
            response = requests.get(str(newpage))
        # reset page count when there are no more pages for a category
        count = 1

    # create a dictionary of recipe attributes and store them in a pandas dataframe
    recipe_dict = {'Title': title, 'Time': time, 'Ingredients': ingredients, 'Link': link, 'Image': image}
    data_frame = pd.DataFrame(recipe_dict)
    # write the dataframe to a csv file
    data_frame.to_csv(output_path, 'w')


if __name__ == '__main__':
    main()