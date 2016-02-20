import requests
import bs4
import csv
import time

movie_list_of_dicts = []

# create master loop for each url
for i in range(1,10):
    # sleep for 1 second.
    time.sleep(1)
    url = "http://www.esquire.com/entertainment/movies/g226/best-movies-ever-0609/?slide={}".format(i)
    
    # get html from url
    html = requests.get(url).content
    soup = bs4.BeautifulSoup(html, "html.parser")

    # get all gallery slides.
    gallery_slides = soup.findAll("div", {"class":"gallery-slide--description--inner"})
    
    # loop through each slide.
    for slide in gallery_slides:
        slide_pargaraph_div = slide.find("div", {"class": "gallery-slide--paragraph"})
        
        if len(slide_pargaraph_div.getText()) > 1 and slide_pargaraph_div:
            # get the text of the h3 tag
            movie_name = slide.find("h3").getText()
            movie_paragraph = slide_pargaraph_div.find("p").text

            # encode values with utf8
            movie_name = movie_name.encode('utf-8')
            movie_paragraph = movie_paragraph.encode('utf-8')

            # insert values into a dictionary.
            movie_dict = { "movie_name": movie_name, 
                           "movie_paragraph": movie_paragraph }
            
            movie_list_of_dicts.append(movie_dict)

# write the csv.
with open('top_movies.csv', 'w') as csvfile:
    fieldnames = movie_list_of_dicts[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for movie_dict in movie_list_of_dicts:
        writer.writerow(movie_dict)