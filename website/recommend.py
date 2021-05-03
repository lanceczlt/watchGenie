from flask import Blueprint, render_template, request, flash, jsonify, session
from .db_connection import connect
import numpy as np 
import pandas as pd 
import scipy.optimize 

connection, cursor = connect()
recommend = Blueprint('recommend', __name__)

cursor.execute('SELECT * FROM users')
users = pd.read_sql('SELECT * FROM users', connection)
ratings = pd.read_sql('SELECT * FROM ratings', connection)
movies = pd.read_sql('SELECT * FROM movies', connection)

movie_ratings = pd.merge(ratings, movies, on='movie_id')[['user_id', 'title', 'movie_id','rating']]

ratings_matrix = movie_ratings.pivot_table(values='rating', index='user_id', columns='title')
ratings_matrix.fillna(0, inplace=True)
movie_index = ratings_matrix.columns

corr_matrix = np.corrcoef(ratings_matrix.T)
corr_matrix.shape

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

# correlation vector of movies
def get_similar_movies(movie_title):
    movie_idx = list(movie_index).index(movie_title)
    return corr_matrix[movie_idx]

def generate_recommendations(user_movies):
    #given a set of movies, it returns all the movies sorted by their correlation with the user
    movie_similarities = np.zeros(corr_matrix.shape[0])
    for movie_id in user_movies:
        movie_similarities = movie_similarities + get_similar_movies(movie_id)
        similar_movies_df = pd.DataFrame({
            'title': movie_index,
            'sum_similarity': movie_similarities
        })
    similar_movies_df = similar_movies_df.sort_values(by=['sum_similarity'], ascending=False)
    return similar_movies_df


def generate_recommendations(userID):
    movie_ratings[movie_ratings.user_id==userID].sort_values(by=['rating'], ascending=False)
    # isolate the user we want to provide an review for
    user_movies = movie_ratings[movie_ratings.user_id==userID].title.tolist()
    recommendations = generate_recommendations(user_movies)
    rec = recommendations.title.head(50)[20:]
    results = []
    for item in rec:
        cursor.execute('SELECT movie_id from movies WHERE title = %s', (str(item)))
        movie = cursor.fetchone()
        results.append(movie['movie_id'])
    return results