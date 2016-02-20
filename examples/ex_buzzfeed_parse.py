# -*- coding: utf-8 -*
import requests
import bs4
import csv

# Step 1: Identify a web page that you want to scrape
url = "http://www.buzzfeed.com/christinebyrne/december-food-2015#.iiQlLaLDp"
# Step 2: Determine what data you will be retrieving
# Step 3: Inspect and Analyze the the website’s structure to learn how you want to get the data.
# Step 4: Think about how you want to structure your data.

# Step 5: request for the page’s content with Python Requests and store the content in a variable.
r = requests.get(url).content

# Step 6: Create a beautiful soup object by passing the variable into the beautiful soup
soup = bs4.BeautifulSoup(r, "html.parser")

# Step 7: Parse/Find your desired content with Beautiful Soup methods.
div_list = soup.findAll({"div" : "buzz_superlist_item"})

recipe_dict_list = []

for div in div_list:
    # narrow divs to those containing rel:buzz_num
    if div.get("rel:buzz_num"): 
        # find the food/recipe name
        sub_buzz_header = div.find("h2", {"class" : "subbuzz_name"})
        if sub_buzz_header:
            recipe_name = sub_buzz_header.text
        
        # find the recipe paragraph
        recipe_para = div.find("p", "sub_buzz_desc_w_attr")
        if recipe_para:
            recipe_link = recipe_para.find("a").get("href")

# Step 8: Transform and Store the data in dictionary format.
        try:
            recipe_dict_list.append({"recipe_name": recipe_name,
                                     "recipe_link": recipe_link})
        except Exception as e:
            pass
# Step 9: Use Python’s CSV module to write a CSV file with the web page’s content.
with open('recipe_list.csv', 'w') as csvfile:
    fieldnames = ['recipe_name', 'recipe_link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for recipe_dict in recipe_dict_list:
        writer.writerow(recipe_dict)