#TODO: add correct shebang to files 

import requests
import time
import json
import os, sys


def get_config(file_path):
    with open(file_path) as f: 
        return json.load(f)

def get_rotten_scores(movie_name):
    movie_url = API_URL.format(ROTTEN_API_KEY,movie_name)
    r = requests.get(movie_url).json()
    return r

# get the current directory of the script
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

# find the config.
CONFIG_NAME = CURRENT_DIR + '/../conf/api_creds.json'
CONFIG = get_config(CONFIG_NAME)

ROTTEN_API_KEY = CONFIG['api_key']
API_URL = "http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey={}&q={}&page_limit=1"

movies = [  "While We're Young"," The Rewrite"," Aloha","Saint Laurent",
            "1/3 of A Little Chaos","Life Partners","Fort Tilden","Adult Beginners",
            "House of Cards","Madame Bovary","Face of an Angel","In Your Eyes",
            "The Immigrant"," 1/2 of Laggies"," Barefoot","Dior and I"]


for movie in movies:
    r = get_rotten_scores(movie)
    time.sleep(1)
    audience_score = 000
    critic_score = 000
    year = 0000
    try:
        audience_score = r['movies'][0]['ratings']['audience_score']
    except:
        pass
    try:
        critic_score = r['movies'][0]['ratings']['critics_score']
    except:
        pass
    try:
        year = r['movies'][0].get('year')
    except:
        pass
    print movie + "| " + str(audience_score) + "| " + str(critic_score) + "| " + str(year)
