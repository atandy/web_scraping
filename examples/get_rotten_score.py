import requests
import time
import json
import os, sys
import csv
from collections import OrderedDict

def get_config(file_path):
    ''' get the config file and load it as json'''
    with open(file_path) as f: 
        return json.load(f)

def get_rotten_scores(movie_name):
    ''' get a response from RT API for a movie name as str '''
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

# example list of movies
movies = [  "While We're Young"," The Rewrite"," Aloha","Saint Laurent",
            "1/3 of A Little Chaos","Life Partners","Fort Tilden","Adult Beginners",
            "House of Cards","Madame Bovary","Face of an Angel","In Your Eyes",
            "The Immigrant"," 1/2 of Laggies"," Barefoot","Dior and I"]

movie_score_dict_list = []

for movie in movies:
    r = get_rotten_scores(movie)
    time.sleep(1)
    # set empty false values in the event the API returns nothing.
    audience_score = 000
    critic_score = 000
    year = 0000

    # try to get values, pass if they are not found. 
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

    d = {
        'movie_name': movie,
        'audience_score': audience_score, 
        'critic_score': critic_score,
        'year': year
    }
    
    movie_score_dict_list.append(OrderedDict(d))
    #print movie + "| " + str(audience_score) + "| " + str(critic_score) + "| " + str(year)

# write the results to a CSV.
with open('movie_scores.csv', 'w') as csvfile:
    fieldnames = movie_score_dict_list[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for movie_score_dict in movie_score_dict_list:
        writer.writerow(movie_score_dict)