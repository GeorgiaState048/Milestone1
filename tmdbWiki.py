import random
import requests
import os
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())


def randomMovie():
    movieList = ['603692', '447365', '493529']
    currMovie = random.choice(movieList)
    TMDB_URL="https://api.themoviedb.org/3/movie/"+currMovie

    query_params = {
        "api_key": os.getenv("API_KEY"),
    }

    response = requests.get(
        TMDB_URL,
        params=query_params
    )
    
    query=response.json()
    movieId=query["id"]
    title=query["title"]
    tagline=query["tagline"]
    genre=query["genres"]
    genres=[]
    for i in genre:
        genres.append(i["name"])
    moviePoster="https://image.tmdb.org/t/p/w500"+query["poster_path"]   

    #MovieWiki:
    BASE_URL="https://en.wikipedia.org/w/api.php"
    query_params = {
        "action": "opensearch",
        "search": title,
    }
    response = requests.get(
        BASE_URL,
        params=query_params
    )

    query1=response.json()
    wikiPage=query1[3][0]

    return [movieId, title, tagline, genres, moviePoster, wikiPage]
