from flask import Blueprint, render_template, request, flash, jsonify, session, redirect, url_for, session
import json
from db_connection import connect


views = Blueprint('views', __name__)
connection, cursor = connect()

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
    if request.method =='GET':
        cursor.execute(
            "SELECT title FROM moviegenie.movies JOIN moviegenie.links WHERE moviegenie.title = %s "
            )
    results = cursor.fetchmany(10)
    



    
    
    return render_template("movie_result.html")






        

