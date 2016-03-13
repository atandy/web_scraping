### OMDB API Integration

To use the OMDB API, all you have to do is make a request to the URL, like this:


http://www.omdbapi.com/?t=titanic&y=&plot=short&r=json

For each movie name you scraped, use the OMDB API to get the

1. `Year`
2. `Metascore`
3. `Writer`

You can view my [get_movie_data.py](https://github.com/atandy/web_scraping/blob/master/examples/get_movie_data.py) for an example of how to get those values from the OMDB API.
