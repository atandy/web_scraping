import requests
import bs4
import csv

movie_list_of_dicts = []
#todo change counter range. 
#todo: remove dupes.
for i in range(1,3):
    url = "http://www.esquire.com/entertainment/movies/g226/best-movies-ever-0609/?slide={}".format(i)
    print url
    r = requests.get(url).content
    soup = bs4.BeautifulSoup(r, "html.parser")

    gallery_slides = soup.findAll("div", {"class":"gallery-slide--description--inner"})
    print gallery_slides
    for slide in gallery_slides:
        slide_pargaraph_div = slide.find("div", {"class": "gallery-slide--paragraph"})
        
        if len(slide_pargaraph_div.getText()) > 1 and slide_pargaraph_div:
            movie_name = slide.find("h3").getText()
            movie_paragraph = slide_pargaraph_div.find("p").text
            movie_dict = { "movie_name": movie_name, 
                           "movie_paragraph": movie_paragraph }
            movie_list_of_dicts.append(movie_dict)
print movie_list_of_dicts