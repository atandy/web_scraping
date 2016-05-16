import requests
import bs4
import csv
url = "http://www.esquire.com/entertainment/movies/g2419/100-best-sci-fi-movies/?slide=1"
requests?
requests.get?
url
response = requests.get(url)
response.status_code
response.text
r = requests.get(url)
html = r.content
r.content?
r.text?
soup = bs4.BeautifulSoup(html, "html.parser")
soup = bs4.BeautifulSoup(html, "html.parser")
soup.findAll?
soup.get?
soup.getText?
soup.findAll('div', {'class':'gallery-slide--title'})
soup.findAll('div', {'class':'gallery-slide--title'})
movies = soup.findAll('div', {'class':'gallery-slide--title'})
movies = soup.findAll('div', {'class':'gallery-slide--title'})
for movie in movies:
    print movie
for movie in movies:
    print movie, print type(movie)
for movie in movies:
    print movie, type(movie)
for movie in movies:
    print movie, type(movie)
for movie in movies:
    text = movie.getText()
for movie in movies:
    text = movie.getText()
    print text
for movie in movies:
    text = movie.getText()
    if len(text) > 0:
        movie_name = text.split('.')[0]
        rank = text.split('.')[0]
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
        print movie_name
text
text.split('.')
text.split('.')[0]
text.split('.')[1]
for movie in movies:
    text = movie.getText()
    movie_name = text.split('.')[1]
    rank = text.split('.')[0]
    print movie_name, rank
for movie in movies:
    text = movie.getText()
    movie_name = text.split('.')[1]
    rank = text.split('.')[0]
    print movie_name, rank
for movie in movies:
    text = movie.getText(); print text
    movie_name = text.split('.')[1]
    rank = text.split('.')[0]
    print movie_name, rank
for movie in movies:
    print movie.getText()
for movie in movies:
    print movie.getText()
    movie.getText().split('.')
for movie in movies:
    print movie.getText()
    movie.getText().split('.')[0]
history
movies
movie_dict_list = []
movie_dict_list = []
%cpaste
movie_dict_list
with open('top_scifi_movies.csv', 'w') as csvfile:
    fieldnames = movie_dict_list[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for movie_dict in movie_dict_list:
        writer.writerow(movie_dict)
