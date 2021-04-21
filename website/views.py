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
        return render_template("home.html")
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

def searchMovies(movie_title):
    cursor.execute('SELECT DISTINCT movies.title, links.imdb_id from movies, links WHERE links.movie_id = movies.movie_id AND movies.title LIKE %s', ("%" + str(title) + "%"))
    return cursor.fetchall()
    
def getTopMovies(genres):
    query = "SELECT DISTINCT movie_id FROM moviegenie.movies WHERE movies.genres LIKE '%s' AND movies.genres LIKE '%s' AND movies.genres LIKE '%s'"
    cursor.execute(query, ("%"+ genres[0] +"%", "%"+ genres[1] +"%", "%"+ genres[2] +"%"))
    df = df(cursor.fetchall())
    df.columns = cursor.column_names
    return df


