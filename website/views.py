from flask import Blueprint, render_template, request, flash, jsonify, session, redirect, url_for, session
import json
import pandas as pd 
import numpy as np 

from .db_connection import connect


views = Blueprint('views', __name__)
connect, cursor = connect()

@views.route('/', methods=['GET', 'POST'])
def home():
    if 'username' in session:
        user_id = session['user_id']
        if hasUserProvidedReviews(user_id):
            # find the movies in the curr_recommendation that has not been watched (reviewed)
            query = "SELECT movie_id FROM moviegenie.users JOIN moviegenie.ratings ON users.user_id = ratings.user_id JOIN moviegenie.curr_recommendation ON users.user_id = curr_recommendation.user_id WHERE users.user_id = '%s' AND (ratings.movie_id IS NULL OR curr_recommendation.movie_id IS NULL)"
            cursor.execute(query, user_id)
            # convert user's movie recs into a list
            movieRecList = list(cursor.fetchall())
            return render_template("home.html", movieRecList)
        else:
            return redirect(url_for('views.search'))
    else:
        return redirect(url_for('auth.login'))

@views.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        movie_id = request.form['movie']
    else:
        return render_template("search.html")

@views.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        movie_id = request.form['movie']

@views.route('/interest_request', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        interests = request.form['movie']
    else:
        return render_template("interest.html")

# given a list of genres and a language, return the top movies
# for the registration user interest learning process
def searchMovies(movie_title):
    cursor.execute('SELECT DISTINCT movies.title, links.imdb_id from movies, links WHERE links.movie_id = movies.movie_id AND movies.title LIKE %s', ("%" + str(title) + "%"))
    return cursor.fetchall()
    
def filterGenres(genres):
    query = "SELECT DISTINCT movie_id FROM moviegenie.movies WHERE movies.genres LIKE '%s' AND movies.genres LIKE '%s' AND movies.genres LIKE '%s'"
    cursor.execute(query, ("%"+ genres[0] +"%", "%"+ genres[1] +"%", "%"+ genres[2] +"%"))
    df = df(cursor.fetchall())
    df.columns = cursor.column_names
    return df

def hasUserProvidedReviews(user_id):
    query = "SELECT count(movie_id) as count FROM moviegenie.users JOIN moviegenie.ratings ON users.user_id = ratings.user_id WHERE users.user_id = '%s'"
    cursor.execute(query, user_id)
    count = cursor.fetchone()['count']
    if count >= 5: 
        return True
    else:
        return False
