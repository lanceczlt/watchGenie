from flask import Flask, render_template, session
from flask_mail import Mail, Message
from os import path
from .db_connection import connect
from flask_session import Session


connect, cursor = connect()
mail = Mail()
sess = Session()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'magical key'
    app.config['SESSION_TYPE'] = 'filesystem'
    sess.init_app(app) 
    app.config['DEBUG'] = True
    #make testing false if u want to be spammed with emails
    app.config['TESTING'] = False
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] =  True
    app.config['MAIL_DEBUG'] = True 
    app.config['MAIL_USERNAME'] = 'watchgenie393@gmail.com'
    ##add password for email later
    app.config['MAIL_PASSWORD'] = 'watchme26'
    app.config['MAIL_DEFAULT_SENDER'] = 'WatchGenie and friends','watchgenie393@gmail.com'
    app.config['MAIL_MAX_EMAILS'] = 10
    app.config['MAIL_SURPRESS_SEND'] =  False
    app.config['MAIL_ASCII_ATTACHMENTS'] = False
    mail.init_app(app)

    msg = Message('Hey There, here is your movie recommendation of the week!',sender="watchgenie393@gmail.com", recipients=['llc52@case.edu'])
    msg.body = 'Check out this!' 
    msg.html = '<b>  <b>' 
    # with app.open_resource('hanjicat.jpg') as look:
    #     msg.attach('hanjicat.jpg', 'image/jpeg', look.read()) 
    with app.app_context():
       mail.send(msg)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    create_database()

    return app

def create_database():
    user = "CREATE TABLE IF NOT EXISTS moviegenie.user ( user_id int(20) NOT NULL, first_name char(50), last_name char(50), email varchar(300), password varchar(50), age int(20), PRIMARY KEY (user_id));"
    movie = "CREATE TABLE IF NOT EXISTS moviegenie.movie ( movie_id int(20) NOT NULL, title varchar(300), genres varchar(500), PRIMARY KEY (movie_id));"
    rating = "CREATE TABLE IF NOT EXISTS moviegenie.rating ( user_id int(20) NOT NULL, movie_id int(20), rating int, PRIMARY KEY (user_id));"
    link = "CREATE TABLE IF NOT EXISTS moviegenie.link ( movie_id int(20) NOT NULL, imdb_id int(20), tmdb_id int, PRIMARY KEY (movie_id));"

    cursor.execute(user)
    cursor.execute(movie)
    cursor.execute(rating)
    cursor.execute(link)
    connect.commit() 

# def send_mail():
#     # user_id = session['id']
#     # cursor.execute('')
#     msg = Message('Hey There, here is your movie recommendation of the week!',sender="superjirachi123@gmail.com", recipients=['llc52@case.edu'])
#     msg.body = 'Movies here'
#     #msg.html = render_template('notify.html')
#     # with open('/static/images/hanjicat.jpg') as look:
#     #     msg.attach('hanjicat.jpg', 'image/jpeg', look.read(), 'inline', headers={'Content-ID' : 'hanjicat'})  #../static/images/hanjicat.jpg

#     mail.send(msg)
#     return "mail sent"


# send_mail()
