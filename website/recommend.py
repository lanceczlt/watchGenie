from flask import Blueprint, render_template, request, flash, jsonify, session
from .db_connection import connect
import numpy as np
import pandas as pd
import scipy.optimize
from surprise import Dataset, Reader, SVD, accuracy
from surprise.model_selection import train_test_split
import matplotlib.pyplot as plt

connection, cursor = connect()

movies = pd.read_sql('SELECT m1.movie_id, title, GROUP_CONCAT(DISTINCT genre_name SEPARATOR \' \') as genres FROM movies as m1 JOIN movie_genre ON m1.movie_id = movie_genre.movie_id JOIN genres ON movie_genre.genre_id = genres.genre_id GROUP BY (m1.movie_id)', connection)
ratings = pd.read_sql(
    'SELECT user_id, movie_id, rating FROM ratings', connection)
tags = pd.read_sql(
    'SELECT movie_id, tag_name as tag FROM movie_tag JOIN tags on movie_tag.tag_id = tags.tag_id', connection)
ratings_f = ratings.groupby('user_id').filter(lambda x: len(x) >= 55)
movie_list_rating = ratings_f.movie_id.unique().tolist()
movies = movies[movies.movie_id.isin(movie_list_rating)]
Mapping_file = dict(zip(movies.title.tolist(), movies.movie_id.tolist()))

mixed = pd.merge(movies, tags, on='movie_id', how='left')
mixed.fillna("", inplace=True)
mixed = pd.DataFrame(mixed.groupby('movie_id')[
                     'tag'].apply(lambda x: "%s" % ' '.join(x)))
Final = pd.merge(movies, mixed, on='movie_id', how='left')
Final['metadata'] = Final[['tag', 'genres']].apply(
    lambda x: ' '.join(x), axis=1)

reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(ratings, reader)
trainset, testset = train_test_split(data, test_size=.25)
algorithm = SVD()
algorithm.fit(trainset)


def generate_recommendations(user_id):
    ui_list = ratings[ratings.user_id == user_id].movie_id.tolist()
    d = {k: v for k, v in Mapping_file.items() if not v in ui_list}
    predictedL = []
    for i, j in d.items():
        predicted = algorithm.predict(user_id, j)
        predictedL.append((i, predicted[3]))
    pdf = pd.DataFrame(predictedL, columns=['movie_title', 'rating'])
    pdf.sort_values('rating', ascending=False, inplace=True)
    pdf.set_index('movie_title', inplace=True)
    results = pdf.head(20)
    movie_recs = results.index.tolist()
    recs = []
    for mov in movie_recs:
        cursor.execute(
            'select movie_id from movies where title = %s order by popularity', str(mov))
        recs.append(cursor.fetchone()['movie_id'])
    return recs
