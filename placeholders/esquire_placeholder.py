#-*- coding: utf-8 -*-
import requests
import bs4
import csv
import time

# NOTE: For this class, I am providing the urls for the pages we will scrape.

# Step 1: Identify page to scrape. 
url = "http://www.esquire.com/entertainment/movies/g2419/100-best-sci-fi-movies/?slide=1"

# Step 2: Determine what data you'll be retrieving.
    # movie_name, rank
# Step 3: Inspect and analyze the website's structure to learn how to get the data.
# Step 4: Think about how you want to structure your data.
# Step 5: request for the page’s content with Python Requests and store the content in a variable.
# Step 6: Create a beautiful soup object by passing the variable into the beautiful soup
# Step 7: Parse/Find your desired content with Beautiful Soup methods.
# Step 8: Transform and Store the data in dictionary format.


# Step 9: Use Python’s CSV module to write a CSV file with the web page’s content.
