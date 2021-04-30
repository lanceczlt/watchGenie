from flask import Blueprint, render_template, request, flash, jsonify, session, redirect, url_for, session
import json


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if 'username' in session:
        return render_template("home.html")
    else:
        return redirect(url_for('auth.login'))

@views.route('/search', methods=['GET', 'POST'])
def search():
<<<<<<< Updated upstream
    return render_template("search.html")
=======
    if request.method == 'POST':
        movie_id = request.form['movie']
    else:
        return render_template("search.html")

@views.route('/result', methods=['GET', 'POST'])
def result():
    if request.method =='GET':
        cursor.execute("SELECT title FROM moviegenie.movies WHERE moviegenie.title = %s ")
    results = cursor.fetchmany(10)

    if request.method == 'POST':
        movie_id = request.form['movie']

    else:
        return render_template("movie_result.html")





        
>>>>>>> Stashed changes

