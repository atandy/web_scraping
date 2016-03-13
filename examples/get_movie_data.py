import json
import requests

movie_title = "titanic"
url = """http://www.omdbapi.com/?t={}&y=&plot=short&r=json""".format(movie_title)

response = requests.get(url).json()
try:
    year = response['Year']
except:
    year = None
try:
    writer = response['Writer']
except:
    writer = None

try:
    metascore = response['Metascore']
except:
    metascore = None


print(year, writer, metascore)