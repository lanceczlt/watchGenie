from flask import Flask, session, render_template
from flask_mail import Mail, Message
from os import path
from .db_connection import connect

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
    app.config['TESTING'] = True
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
    msg.body = 'Movies here' 
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
