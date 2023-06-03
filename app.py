import flask
import random
import requests
import os
import tmdbWiki
from dotenv import find_dotenv, load_dotenv

app = flask.Flask(__name__)

@app.route('/')
def index():
    data = tmdbWiki.randomMovie()
    myGenres = ""
    for i in range(len(data[3])):
        if i == len(data[3]):
            myGenres += data[3][i]
        else:
            myGenres += data[3][i] + ","
    
    return flask.render_template(
        "index.html", 
        movieId=data[0],
        title=data[1],
        tagline=data[2],
        genres=data[3],
        moviePoster=data[4],
        wikiPage=data[5]
    )

app.run(
    debug=True
)
