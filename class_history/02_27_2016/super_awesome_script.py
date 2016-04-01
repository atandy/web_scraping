#import modules
import requests
import csv
import bs4

# create empty list to hold all the dictionaries
movie_dict_list = []

for number in range(1, 15):
    #set the url
    url = "http://www.esquire.com/entertainment/movies/g2419/100-best-sci-fi-movies/?slide={}".format(number)

    # generate a request
    request = requests.get(url)

    # create a beautiful soup object.
    soup = bs4.BeautifulSoup(request.content, "html.parser")

    # create list of bs4 Tags as variable named "movies"
    movies  = soup.findAll('div', {'class':'gallery-slide--title' })

    for movie in movies:
        # get the text
        text = movie.getText()
        if len(text) > 0:
            movie_rank = text.split('.')[0].encode('utf-8')
            movie_name = text.split('.')[1].encode('utf-8')

            # create a dictionary with two keys, assign values from text above.
            d = {
                'movie_name': movie_name, 
                'movie_rank': movie_rank 
            }

            # append the dictionary to the master list. 
            movie_dict_list.append(d)

# create a CSV using python's CSV module. 
# open the file in write-mode and alias it as 'csvfile'
with open('top_scifi_movies.csv', 'w') as csvfile:
    # set the fieldnames for the csvwriter.
    fieldnames = movie_dict_list[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # write the header to the csv file.
    writer.writeheader()

    # for each movie dictionary in the master list, write a row to the csv file.
    for movie_dict in movie_dict_list:
        writer.writerow(movie_dict)



