from flask import Flask, session
from os import path
from .db_connection import connect
from flask_session import Session 

connect, cursor = connect()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'magical key'
    app.config['SESSION_TYPE'] = 'filesystem'
    sess = Session()
    sess.init_app(app) 

    from .views import views
    from .auth import auth
    from .visualize import visualize

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(visualize, url_pref='/')
    return app

