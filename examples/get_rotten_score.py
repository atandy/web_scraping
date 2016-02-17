#TODO: add correct shebang to files 

import requests
import time
import json

def get_config(file_path):
    with open(file_path) as f: 
        return json.load(f)

def get_rotten_scores(movie_name):
    movie_url = API_URL.format(ROTTEN_API_KEY,movie_name)
    r = requests.get(movie_url).json()
    return r


CONFIG_NAME = 'api_creds.json'
CONFIG = get_config(CONFIG_NAME)
ROTTEN_API_KEY = CONFIG['api_key']
API_URL = "http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey={}&q={}&page_limit=1"


'''
movies = [ "In the Heat of the Night","Slap Shot","Iron Man","Jaws","Save the Tiger",
           "12 Angry Men","Fast Times at Ridgemont High","Chinatown","The Godfather",
           "Fitzcarraldo","Ghostbusters","Glory","Wall Street","Runaway Train","Rosemary's Baby",
           "North by Northwest","Lone Star","The Good, the Bad and the Ugly","The Conversation",
           "The Thin Blue Line","Johnny Dangerously","The French Connection","Miller's Crossing",
           "The Great Escape","Dawn of the Dead","Shaun of the Dead","Hate","First Blood","Bottle Rocket",
           "Bad Day at Black Rock","Tootsie","Broadcast News","The Terminator","Shakes the Clown",
           "Dirty Harry","Straw Dogs","Raging Bull","Citizen Kane","The Shining","Fatal Attraction",
           "The Incredibles","Blade Runner","Sling Blade","Giant","Glengarry Glen Ross","Serpico",
           "Down by Law","The Searchers","Do the Right Thing","Gone Baby Gone","The Big Kahuna","M*A*S*H",
           "The Verdict","The Warriors","Alien","Stalag 17","Bridge on the River Kwai","The Misfits",
           "Reservoir Dogs","The Maltese Falcon","Dr. No","Cool Hand Luke","The Road Warrior","Patton",
           "True Romance","Run Silent, Run Deep","All Quiet on the Western Front","Platoon","Caddyshack",
           "Hud","Blazing Saddles","Three Kings","Paths of Glory"]
'''
#movies = ["Me Earl and The Dying Girl"]
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
