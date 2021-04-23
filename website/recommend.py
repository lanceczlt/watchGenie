from flask import Blueprint, render_template, request, flash, jsonify, session
import numpy as np 
import pandas as pd 
import scipy.optimize 
from .db_connection import connect

connect, cursor = connect()
recommend = Blueprint('recommend', __name__)

@recommend.route('/recommend', methods=['GET','POST'])
def recommend(user_id):
    if request.method == 'POST':
        return render_template("recommendation.html")         
    return render_template("recommendation.html")

# given a list of genres and a language, return the top movies
# for the registration user interest learning process
def getTopMovies(genres, language):
    return None

def content_based_rec():
    return None

def plot_based_rec():
    return None

def collaboration_based_rec():
    return None

def searchMovies(movie_title):
    cursor.execute('SELECT DISTINCT movies.title, links.imdb_id from movies, links WHERE links.movie_id = movies.movie_id AND movies.title LIKE %s', ("%" + str(title) + "%"))
    return cursor.fetchall()
    
def getTopMovies(genres):
    query = "SELECT DISTINCT movie_id FROM moviegenie.movies WHERE movies.genres LIKE '%s' AND movies.genres LIKE '%s' AND movies.genres LIKE '%s'"
    cursor.execute(query, ("%"+ genres[0] +"%", "%"+ genres[1] +"%", "%"+ genres[2] +"%"))
    df = df(cursor.fetchall())
    df.columns = cursor.column_names
    return df

