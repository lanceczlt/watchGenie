from flask import Flask, session
from os import path
from .db_connection import connect

connect, cursor = connect()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'magic'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    create_database()

    return app

def create_database():
    user = "CREATE TABLE IF NOT EXISTS moviegenie.User ( user_id int(20) NOT NULL, first_name char(50), last_name char(50), email varchar(300), password varchar(50), age int(20), PRIMARY KEY (user_id));"
    movie = "CREATE TABLE IF NOT EXISTS moviegenie.Movie ( movie_id int(20) NOT NULL, title varchar(300), genres varchar(500), PRIMARY KEY (movie_id));"
    rating = "CREATE TABLE IF NOT EXISTS moviegenie.Rating ( user_id int(20) NOT NULL, movie_id int(20), rating int, PRIMARY KEY (user_id));"
    link = "CREATE TABLE IF NOT EXISTS moviegenie.Link ( movie_id int(20) NOT NULL, imdb_id int(20), tmdb_id int, PRIMARY KEY (movie_id));"

    cursor.execute(user)
    cursor.execute(movie)
    cursor.execute(rating)
    cursor.execute(link)
    connect.commit()