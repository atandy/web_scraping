#-*- coding: utf-8 -*-
import requests
import bs4
import csv
import time

# create empty list to hold all dictionaries.
movie_dict_list = []

# set master loop for total number of movies in listicle
for number in range(1,5):
    time.sleep(1)
    url = "http://www.esquire.com/entertainment/movies/g2419/100-best-sci-fi-movies/?slide={}".format(number)
    # make request
    r = requests.get(url)
    # get the content 
    html = r.content

    # Step 6: Create a beautiful soup object by passing the variable into the beautiful soup
    soup = bs4.BeautifulSoup(html, "html.parser")

    # Step 7: Parse/Find your desired content with Beautiful Soup methods.
    movies = soup.findAll('div', {'class':'gallery-slide--title' })

    for movie in movies:
        text = movie.getText()
        if len(text) > 0:
            movie_name = text.split('.')[1]
            rank = text.split('.')[0]
            movie_name = movie_name.encode('utf-8')
            rank = rank.encode('utf-8')

            # Step 8: Transform and Store the data in dictionary format.
            d = {'movie_name': movie_name, 'rank': rank}
            movie_dict_list.append(d)

# Step 9: Use Python’s CSV module to write a CSV file with the web page’s content.
with open('top_scifi_movies.csv', 'w') as csvfile:
    fieldnames = movie_dict_list[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for movie_dict in movie_dict_list:
        writer.writerow(movie_dict)
