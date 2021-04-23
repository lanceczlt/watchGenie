from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'stmp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
#app.config['MAIL_DEBUG'] = True 
app.config['MAIL_USERNAME'] = 'superjirachi123@gmail.com'
#add password for email later
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_DEFAULT_SENDER'] = 'superjirachi123@gmail.com'
app.config['MAIL_MAX_EMAILS'] = 10
#app.config['MAIL_SURPRESS_SEND'] =  False
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)

@app.route('/')
def index():
    msg = Message('Hey There, here is your movie recommendation of the week!', recipients=['llc52@case.edu'])
    mail.send(msg)

    return 'Message has been sent!'

if __name__ == '__main__':
    app.run(debug = True)
