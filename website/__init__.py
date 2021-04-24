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
    
    return app

