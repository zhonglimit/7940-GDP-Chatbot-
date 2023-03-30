import os
import requests
import logging
# class Movie:

#     Title = ''
#     Year = ''
#     Rated = ''
#     Released = ''
#     Runtime = ''
#     Genre = ''
#     Director = ''
#     Writer = ''
#     Actors = ''
#     Plot = ''
#     Language = ''
#     Country = ''
#     Awards = ''
#     Poster = ''
#     Ratings = []
#     Metascore = ''
#     imdbRating = ''
#     imdbVotes = ''
#     imdbID = ''
#     Type = ''
#     DVD = ''
#     BoxOffice = ''
#     Production = ''
#     Website = ''
#     Response =''

#     def __init__(self,response):
#         return

# def toString(self):
#     print("%s 说: 我 %d 岁。" %(self.name,self.age))
#     return


def get_movie_info(movieTitle):
    url = 'http://www.omdbapi.com/'
    api_key = '5e6f7556'
    data = {'apikey': api_key, 't': movieTitle}
    response = requests.get(url, data).json()

    return None if response.get("Response") != "True" else response
