In [72]: history
url = "declare the encoding of
a Python source file. The encoding information is then used by the
url = "http://www.esquire.com/entertainment/movies/g2419/100-best-sci-fi-movies/?slide=1"
import requests
import csv
import bs4
request = requests.get(url)
request.content?
request.content
soup = bs4.BeautifulSoup(request.content, "html.parser")
bs4.BeautifulStoneSoup?
bs4.Beautifuloup?
bs4.BeautifulSoup?
soup
type(soup)
type(request)
%history
history
soup.findAll('div', {'class':'gallery-slide--title' })
request
request.content
soup.findAll('div', {'class':'gallery-slide--title' })
movies  = soup.findAll('div', {'class':'gallery-slide--title' })
movies
movies[0]
movies[2]
test_movie  = movies[2]
test_movie
type(test_movie)
test_movie.
test_movie.getText()
history
type(test_movie)
test_movie.getText()
for movie in movies:
    print movie
for movie in movies:
    print movie.getText()
movies[2].getText()
test_movie
test_movie.getText()
movie_text = test_movie.getText()
movie_text.split('.')
movie_text.split('.')[0]
movie_text.split('.')[1]
movies
rank = movie_text.split('.')[0]
title = movie_text.split('.')[1]
rank
title
movie
movies
for movie in movies:
    print movie.getText()
moviemovie_dict_list = []
movie_dict_list = []
for movie in movies:
        # get the text
        text = movie.getText()
        if len(text) > 0:
                movie_rank = text.split('.')[0]
                movie_name = text.split('.')[1]
        # create a dictionary with two keys, assign values from text above.
        d = {
            'movie_name': movie_name,
            'movie_rank': movie_rank
        }
        # append the dictionary to the master list.
        movie_dict_list.append(d)
print movie_dict_list
movie_dict_list[0]
movie_dict_list[0].keys()
for number in range(1, 101):
    print number
%history
movie_dict_list
import pandas as pd
pd.DataFrame(movie_dict_list)
df  = pd.DataFrame(movie_dict_list)
df.to_html()
df.to_csv('great.csv')
ls
open great.csv
history
