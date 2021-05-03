from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .db_connection import connect, get_movie_image
from .recommend import generate_recommendations
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

        parameters = []
        filtering_query = ''

        if genre != '':
            filtering_query += ' AND genre_name = %s'
            parameters.append(genre)
        if release_date != '':
            filtering_query += ' AND year(release_date) >= %s'
            parameters.append(release_date)
        if avg_vote != '':
            filtering_query += ' AND vote_average >= %s'
            parameters.append(avg_vote)
        if title != '':
            filtering_query += ' AND MATCH(title) AGAINST (%s IN NATURAL LANGUAGE MODE)'
            parameters.append(title)
        search_query = "SELECT distinct m1.movie_id, title, overview, budget, popularity, release_date, revenue, duration, vote_average, vote_count FROM movies as m1 JOIN movie_genre ON m1.movie_id=movie_genre.movie_id JOIN genres ON movie_genre.genre_id=genres.genre_id WHERE '' = '' " + filtering_query + ' GROUP BY movie_id ORDER BY popularity desc LIMIT 20'
        cursor.execute(search_query, tuple(parameters))
        search_results=cursor.fetchall()
        print(len(search_results))
        for result in search_results:
            result['img_url']=get_movie_image(result['movie_id'])
        session['results'] = search_results
        return redirect(url_for('views.result'))
    else:
        return render_template("search.html")

@ views.route('/result', methods=['GET', 'POST'])
def result():
    search_results = session['results']
    session.pop('results', None)
    return render_template('search_result.html', search_results=search_results)

@ views.route('/movie_info/', methods=['GET', 'POST'])
@ views.route('/movie_info/<movie_id>', methods=['GET', 'POST'])
def movie_info(movie_id=None):
    movie_query="select * from movies where movie_id = %s"
    cursor.execute(movie_query, movie_id)
    movie_info=cursor.fetchone()
    movie_info['img_url']=get_movie_image(movie_id)
    return render_template('movie_info.html', info=movie_info)

@ views.route('/recommendation', methods=['GET', 'POST'])
def recommendation():
    if request.method == "POST": 
        gen_recs = generate_recommendations(1)
        for rec in gen_recs:
                cursor.execute("INSERT INTO user_rec(user_id, movie_id, have_watched, current_rec) VALUES (%s,%s,%s,%s)", (1, rec, '0', '0'))
                
    rec_query="select * from users join user_rec on users.user_id = user_rec.user_id where users.user_id = %s"
    cursor.execute(rec_query, '1')
    mov_recs = cursor.fetchall()
    for rec in mov_recs:
                rec['img_url'] = get_movie_image(rec['movie_id'])
    return render_template('recommendation.html', search_results = mov_recs)