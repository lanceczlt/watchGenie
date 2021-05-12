from flask import Blueprint, render_template, request, flash, jsonify, session
from .db_connection import connect
import numpy as np 
import pandas as pd 
import scipy.optimize 
from collections import OrderedDict
from numpy import dot
connection, cursor = connect()

cursor.execute('SELECT * FROM users')
users = pd.read_sql('SELECT * FROM users', connection)
ratings = pd.read_sql('SELECT * FROM ratings', connection)
movies = pd.read_sql('SELECT * FROM movies', connection)

movie_genres = pd.read_sql('SELECT m1.movie_id, title, GROUP_CONCAT(DISTINCT genre_name SEPARATOR \'|\') as genres FROM movies as m1 JOIN movie_genre ON m1.movie_id = movie_genre.movie_id JOIN genres ON movie_genre.genre_id = genres.genre_id GROUP BY (m1.movie_id)', connection)
movie_genres = pd.concat([movie_genres, movie_genres.genres.str.get_dummies(sep='|')], axis=1)

movie_categories = movie_genres.columns[3:]

movie_ratings = pd.merge(ratings, movies, on='movie_id')[['user_id', 'title', 'movie_id','rating']] 
#matrix of users and their associated ratings
ratings_matrix = movie_ratings.pivot_table(values='rating', index='user_id', columns='title')
ratings_matrix.fillna(0, inplace=True)
movie_index = ratings_matrix.columns

# uses pearson's product corellation coefficient to calculate movie similarities
# correlation value between -1 and 1
correlation_matrix = np.corrcoef(ratings_matrix.T)

def get_user_preferences(user_genres):
    user_preferences = OrderedDict(zip(movie_categories, []))
    for key in user_preferences:
        key = 0
    for gen in user_genres:
        user_preferences[str(gen['genre_name'])] = gen['cnt']
    return user_preferences

def get_movie_score(movie_features, user_preferences):  
    return dot_product(movie_features, user_preferences)

def dot_product(vector_1, vector_2):  
    return sum([ i*j for i,j in zip(vector_1, vector_2)])

def get_movie_recommendations_content(user_id):  
    cursor.execute('SELECT genre_name, count(movies.movie_id) as cnt from movies join movie_genre as mg on movies.movie_id = mg.movie_id join genres on mg.genre_id = genres.genre_id join ratings on movies.movie_id = ratings.movie_id where user_id = %s group by genre_name', user_id)
    user_preferences = get_user_preferences(cursor.fetchall())
    movie_genres['score'] = movie_genres[movie_categories].apply(get_movie_score, args=([user_preferences.values()]), axis=1)
    movie_genres.sort_values(by=['score'], ascending=False)['title']
    return movie_genres['movie_id'].head(30).tolist()


# get closest movies in the correlation matrix
def closest_movies(movie_title):
    movie_idx = list(movie_index).index(movie_title)
    return correlation_matrix[movie_idx]

def collaborative_filtering_movies(user_movies):
    #given a set of movies, it returns all the movies sorted by their correlation with the provided user
    similarities = np.zeros(correlation_matrix.shape[0])
    for movie_id in user_movies:
        similarities = similarities + closest_movies(movie_id)
        correlated_movies = pd.DataFrame({'title': movie_index, 'sum_similarity': similarities})
    correlated_movies = correlated_movies.sort_values(by=['sum_similarity'], ascending=False)[:30]
    return correlated_movies


def generate_recommendations(userID):
    movie_ratings[movie_ratings.user_id==userID].sort_values(by=['rating'], ascending=False)
    user_movies = movie_ratings[movie_ratings.user_id==userID].title.tolist()
    recommendations = collaborative_filtering_movies(user_movies)
    rec = recommendations.title.head(30)
    recommendations = []
    for item in rec:
        cursor.execute('SELECT movie_id from movies WHERE title = %s', (str(item)))
        movie = cursor.fetchone()
        recommendations.append(movie['movie_id'])
    return recommendations