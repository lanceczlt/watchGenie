from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .db_connection import connect, get_movie_image
import json

views = Blueprint('views', __name__)
connect, cursor = connect()

search_results = []

@views.route('/', methods=['GET', 'POST'])
def landing():
    return render_template("landing.html")

@views.route('/home', methods=['GET', 'POST'])
def home():
    return render_template("homepage.html")

@views.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        genre = request.form.get('genres')
        release_date = request.form.get('release_year')
        avg_vote = request.form.get('avg_vote')
        title = request.form.get('movie_title')
        search_query = "select * from movies JOIN movie_genre ON movies.movie_id = movie_genre.movie_id JOIN genres ON movie_genre.genre_id = genres.genre_id JOIN links ON movies.movie_id = links.movie_id WHERE genre_name = %s AND year(release_date) >= %s AND vote_average >= %s AND MATCH(title) AGAINST(%s IN NATURAL LANGUAGE MODE)"
        cursor.execute(search_query,(genre, release_date, avg_vote, title))
        search_results = cursor.fetchall()
        for result in search_results:
            result['img_url'] = get_movie_image(result['movie_id'])
        session['results'] = search_results
        print(type(session['results']))
        return redirect(url_for('views.result'))
    else:
        return render_template("search.html")

@views.route('/result', methods=['GET', 'POST'])
def result():
    return render_template('search_result.html', search_results = session['results'])


