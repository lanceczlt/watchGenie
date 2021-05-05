from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .db_connection import connect, get_movie_image
from .recommend import generate_recommendations
from .visualize import userBubbleChart, userCompareBar, userGenrePie
from datetime import datetime
import dateutil.relativedelta
import json

views = Blueprint('views', __name__)
connection, cursor = connect()

search_results = []


@views.route('/', methods=['GET', 'POST'])
def landing():
    if 'username' in session:
        return redirect(url_for('views.home'))
    return render_template("landing.html")


@views.route('/home', methods=['GET', 'POST'])
def home():
    if 'username' not in session:
        flash('Please login first!')
        return redirect(url_for('auth.login'))
    current_date = datetime.now()
    # get last month's date in order to give the currently popular movies
    last_month = current_date + dateutil.relativedelta.relativedelta(years=-1)
    cursor.execute("select m.movie_id, title, overview, popularity, release_date, runtime, vote_average from (select distinct movies.movie_id, avg(rating) as avg_rating from ratings join movies on movies.movie_id = ratings.movie_id where rating_date >= %s group by movies.movie_id order by count(movies.movie_id)) as m join movies on movies.movie_id = m.movie_id where avg_rating > 3.5 LIMIT 10", (last_month))
    trending = cursor.fetchall()
    cursor.execute("select movies.movie_id, title, overview, popularity, release_date, runtime, vote_average from movies join ratings on movies.movie_id = ratings.movie_id order by rating_date desc limit 10")
    latest = cursor.fetchall()

    for movie in trending:
        movie['img_url']=get_movie_image(movie['movie_id'])

    for movie in latest:
        movie['img_url']=get_movie_image(movie['movie_id'])
    return render_template("homepage.html", trending = trending, latest = latest)


@views.route('/search', methods=['GET', 'POST'])
def search():
    if 'username' not in session:
        flash('Please login first!')
        return redirect(url_for('auth.login'))
    if request.method == "POST":
        genre = request.form.get('genres')
        year_start = request.form.get('release_year_start')
        year_end = request.form.get('release_year_end')
        avg_vote = request.form.get('avg_vote')
        title = request.form.get('movie_title')

        parameters = []
        filtering_query = ''
        if(year_start > year_end):
            flash('Please have your start date before your end date.')
            return render_template("search.html")
        if genre != '':
            filtering_query += ' AND genre_name = %s'
            parameters.append(genre)
        if year_start != '':
            filtering_query += ' AND year(release_date) >= %s'
            parameters.append(year_start)
        if avg_vote != '':
            filtering_query += ' AND vote_average >= %s'
            parameters.append(avg_vote)
        if title != '':
            filtering_query += ' AND MATCH(title) AGAINST (%s IN NATURAL LANGUAGE MODE)'
            parameters.append(title)
        search_query = "SELECT distinct m1.movie_id, title, overview, popularity, release_date, runtime, vote_average FROM movies as m1 JOIN movie_genre ON m1.movie_id=movie_genre.movie_id JOIN genres ON movie_genre.genre_id=genres.genre_id WHERE '' = '' " + filtering_query + ' GROUP BY movie_id LIMIT 20'
        cursor.execute(search_query, tuple(parameters))
        search_results=cursor.fetchall()
        if len(search_results) != 0:
            for result in search_results:
                result['img_url']=get_movie_image(result['movie_id'])
            session['results'] = search_results
            return redirect(url_for('views.result'))
        else:
            flash('Sorry, we got nothing! Please try again!', category='error')
    return render_template("search.html")

@ views.route('/result', methods=['GET', 'POST'])
def result():
    if 'username' not in session:
        flash('Please login first!')
        return redirect(url_for('auth.login'))
    search_results = session['results']
    session.pop('results', None)
    return render_template('search_result.html', search_results=search_results)

@ views.route('/movie_info/', methods=['GET', 'POST'])
@ views.route('/movie_info/<movie_id>', methods=['GET', 'POST'])
def movie_info(movie_id=None):
    if 'username' not in session:
        flash('Please login first!')
        return redirect(url_for('auth.login'))
    if request.method == 'POST':
        rating = request.form.get('rating')
        cursor.execute('INSERT INTO ratings(user_id, movie_id, rating, rating_date) VALUES (%s,%s,%s,%s)',(session['id'], movie_id, rating, datetime.now())) 
        connection.commit()
        session['ratings_provided'] += 1
        flash('Rating updated!')

    cursor.execute("select * from movies where movie_id = %s", movie_id)
    movie_info=cursor.fetchone()
    movie_info['img_url']=get_movie_image(movie_id)

    cursor.execute("SELECT * FROM ratings JOIN movies on movies.movie_id = ratings.movie_id WHERE movies.movie_id = %s AND ratings.user_id = %s", (movie_id, session['id']))
    user_rating = cursor.fetchone()
    if user_rating:
        return render_template('movie_info.html', info=movie_info, user_rating = user_rating['rating'])
    return render_template('movie_info.html', info=movie_info, user_rating = 2.5)

@ views.route('/recommendation/', methods=['GET', 'POST'])
@ views.route('/recommendation/<action>', methods=['GET', 'POST'])
def recommendation(action = None):
    if 'username' not in session:
        flash('Please login first!')
        return redirect(url_for('auth.login'))
    if session['ratings_provided'] < 5:
            flash('Please provide at least 5 ratings before you can generate any recommendations or see your data!')
            return redirect(url_for('views.search'))
    if action == 'update':
        gen_recs = generate_recommendations(session['id'])
        for rec in gen_recs:
            cursor.execute("INSERT INTO cur_rec(user_id, movie_id, have_watched) VALUES (%s,%s,%s)", (session['id'], rec, 0))
            connection.commit()
        for rec in gen_recs:
                rec['img_url'] = get_movie_image(rec['movie_id']) 
        return render_template('recommendation.html', search_results = gen_recs, title = 'New recommendations generated! MAGIC!')
    elif action == 'previous':
        cursor.execute('select distinct movies.movie_id, title, overview, popularity, release_date, runtime, vote_average from prev_rec join users on prev_rec.user_id = users.user_id join movies on movies.movie_id = prev_rec.movie_id where users.user_id = %s', session['id'])
        prev_recs = cursor.fetchall()
        for rec in prev_recs:
                rec['img_url'] = get_movie_image(rec['movie_id'])   
        return render_template('recommendation.html', search_results = prev_recs, title = 'Here are some older recommendations')
    elif action == 'ratings':
        cursor.execute('select distinct movies.movie_id, title, overview, popularity, release_date, runtime, vote_average from ratings join users on ratings.user_id = users.user_id join movies on movies.movie_id = ratings.movie_id where users.user_id = %s', session['id'])
        prev_ratings = cursor.fetchall()
        for rec in prev_ratings:
                rec['img_url'] = get_movie_image(rec['movie_id'])
        return render_template('recommendation.html', search_results = prev_ratings, title = 'Movies you have rated previously')            
    rec_query="select * from users join cur_rec on users.user_id = cur_rec.user_id where users.user_id = %s"
    cursor.execute(rec_query, session['id'])
    mov_recs = cursor.fetchall()
    for rec in mov_recs:
                rec['img_url'] = get_movie_image(rec['movie_id'])
    return render_template('recommendation.html', search_results = mov_recs, title = 'Current recommendations!')

@views.route('/visualization', methods=['GET', 'POST'])
def user_visualization():
    if 'username' not in session:
        flash('Please login first!')
        return redirect(url_for('auth.login'))
    if session['ratings_provided'] < 5:
            flash('Please provide at least 5 ratings before you can generate any recommendations or see your data!')
            return redirect(url_for('views.search'))
    pie1 = userGenrePie()
    bar1 = userCompareBar()
    bubble1 = userBubbleChart()
    return render_template('visualize.html', plot1 = pie1, plot2 = bar1, plot3 = bubble1)