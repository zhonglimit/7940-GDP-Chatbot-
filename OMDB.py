import requests
import os

def get_movie_info(movieTitle):
    url = 'http://www.omdbapi.com/'
    api_key = os.environ["API_KEY"]
    data = {'apikey': api_key, 't': movieTitle}
    response = requests.get(url, data).json()

    return None if response.get("Response") != "True" else response
