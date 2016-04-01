import json
import requests

movie_title = "titanic"
url = """http://www.omdbapi.com/?t={}&y=&plot=short&r=json""".format(movie_title)

response = requests.get(url).json()

year = response.get('Year')
writer = response.get('Writer')
metascore = response.get('Metascore')

print(year, writer, metascore)
