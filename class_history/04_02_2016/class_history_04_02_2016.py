import requests
import bs4
import csv
import requests
requests?
url = "http://www.esquire.com/entertainment/movies/g2419/100-best-sci-fi-movies/?slide=1"
history
r = requests.get(url)
r.status_code?
r = http:/wewranekanfwefawe
r.status_code?
r.content?
r.text?
r.content
content = r.content
type(content)
r = requests.get(url)
content = r.content
from bs4 import BeautifulSoup
import bs4
soup = bs4.BeautifulSoup(content)
history
soup = bs4.BeautifulSoup(content)
type(soup)
soup.findNext?
soup = bs4.BeautifulSoup(content, "html.parser")
soup.findAll?
soup.findAll('div')
soup.findAll?
movies = soup.findAll('div', {'class':'gallery-slide--title' })
movies
soup.select?
soup.select("#site-wrapper > div.gallery-wrapper > div.gallery > div.gallery-shell > div.gallery-container > div.gallery-view-container > div.gallery-slideshow-shell > div > div.gallery-slideshow--container > div.gallery-slide.gallery-slide--curr.horizontal > div.gallery-slide--description > div.gallery-slide--description-wrapper > div.gallery-slide--description--inner > div.gallery-slide--title > h3")
ls
movies
movies
for movie in movies:
    print movie.getText()
for movie in movies:
    print movie.getText()
movies = soup.findAll('div', {'class':'gallery-slide--title' })
for movie in movies:
    print movie.getText()
d = {}
for movie in movies:
    text = movie.getText()
    if len(text) > 0:
        movie_name = text.split('.')[1]
        rank = text.split('.')[0]
for movie in movies:
    text = movie.getText()
    if len(text) > 0:
        movie_name = text.split('.')[1]
        rank = text.split('.')[0]
        print movie_name, rank
for movie in movies:
    text = movie.getText()
    if len(text) > 0:
        movie_name = text.split('.')[1]
        rank = text.split('.')[0]
        print movie_name, rank
history
movies
for movie in movies:
    text = movie.getText()
    if len(text) > 0:
        movie_name = text.split('.')[1]
        rank = text.split('.')[0]
        print movie_name, rank
for movie in movies:
        text = movie.getText()
        if len(text) > 0:
                movie_name = text.split('.')[1]
                movie_rank = text.split('.')[0]
                # create a dictionary with two keys, movie_name and movie_rank
                d = {"movie_name": movie_name, "movie_rank": movie_rank}
                print d
%cpaste
dict_list = []
%cpaste
dict_list[0].keys()
csv.DictWriter?
%cpaste
ls
range(1, 5)
for i in range(1, 5)
for i in range(1, 5):
    print i
for i in range(1, 5):
        url = "http://www.esquire.com/entertainment/movies/g2419/100-best-sci-fi-movies/?slide={}".format(i)
    print url
%cpase
%cpaste
