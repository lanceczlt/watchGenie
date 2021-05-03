import plotly
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go
from flask import Blueprint, render_template, request, flash, jsonify, session
from .db_connection import connect

import pandas as pd
import numpy as np
import json

visualize = Blueprint('visualize', __name__)
connection, cursor = connect()
genreList = ['Animation', 'Comedy', 'Family', 'Adventure', 'Fantasy', 'Romance', 'Drama', 'Action', 'Crime', 'Thriller', 'Horror', 'History', 'Science Fiction', 'Mystery', 'War', 'Foreign', 'Music', 'Documentary', 'Western', 'TV Movie']

@visualize.route('/visualization', methods=['GET', 'POST'])
def user_visualization():
    pie1 = userGenrePie()
    bar1 = userCompareBar()
    bubble1 = userBubbleChart()
    return render_template('visualize.html', plot1 = pie1, plot2 = bar1, plot3 = bubble1)

def userGenrePie():
    user_id = session['id']
    cursor.execute("SELECT genre_name FROM movies JOIN ratings ON movies.movie_id = ratings.movie_id JOIN users ON users.user_id = ratings.user_id JOIN movie_genre ON movies.movie_id = movie_genre.movie_id JOIN genres ON movie_genre.genre_id = genres.genre_id WHERE users.user_id = %s",(user_id))
    genresListDict = cursor.fetchall()
    genres = []
    for element in genresListDict:
        genres.append(element['genre_name'])
    
    animationCount = genres.count('Animation')
    comedyCount = genres.count('Comedy')
    familyCount = genres.count('Family')
    adventureCount = genres.count('Adventure')
    fantasyCount = genres.count('Fantasy')
    romanceCount = genres.count('Romance')
    dramaCount = genres.count('Drama')
    actionCount = genres.count('Action')
    crimeCount = genres.count('Crime')
    thrillerCount = genres.count('Thriller')
    horrorCount = genres.count('Horror')
    historyCount = genres.count('History')
    sciencefictionCount = genres.count('Science Fiction')
    mysteryCount = genres.count('Mystery')
    warCount = genres.count('War')
    foreignCount = genres.count('Foreign')
    musicCount = genres.count('Music')
    documentaryCount = genres.count('Documentary')
    westernCount = genres.count('Western')
    tvmovieCount = genres.count('TV Movie')

    genreCountList = [
        animationCount, 
        comedyCount, 
        familyCount, 
        adventureCount, 
        fantasyCount, 
        romanceCount, 
        dramaCount, 
        actionCount, 
        crimeCount, 
        thrillerCount, 
        horrorCount, 
        historyCount, 
        sciencefictionCount, 
        mysteryCount, 
        warCount, 
        foreignCount, 
        musicCount, 
        documentaryCount, 
        westernCount, 
        tvmovieCount
    ]

    copyGenreList = genreList.copy()

    index = 0
    while index < len(copyGenreList):
        if genreCountList[index] == 0:
            genreCountList.pop(index)
            copyGenreList.pop(index)
            index = index - 1
        index = index + 1

    #pie chart
    d = {'Genre': copyGenreList, 'Count': genreCountList}
    df = pd.DataFrame(data=d)
    fig = px.pie(df, values = 'Count', names = 'Genre', template='plotly_dark').update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    fig.update_layout(height = 600, width = 1400, title_text="Your Genres")
    graphJSON = plotly.io.to_json(fig)
    return graphJSON

def userCompareBar():
    #bar chart comparison
    user_id = session['id']
    cursor.execute("SELECT genre_name FROM movies JOIN ratings ON movies.movie_id = ratings.movie_id JOIN users ON users.user_id = ratings.user_id JOIN movie_genre ON movies.movie_id = movie_genre.movie_id JOIN genres ON movie_genre.genre_id = genres.genre_id WHERE users.user_id = %s",(user_id))
    genresListDict = cursor.fetchall()
    genres = []
    for element in genresListDict:
        genres.append(element['genre_name'])
    
    animationCount = genres.count('Animation')
    comedyCount = genres.count('Comedy')
    familyCount = genres.count('Family')
    adventureCount = genres.count('Adventure')
    fantasyCount = genres.count('Fantasy')
    romanceCount = genres.count('Romance')
    dramaCount = genres.count('Drama')
    actionCount = genres.count('Action')
    crimeCount = genres.count('Crime')
    thrillerCount = genres.count('Thriller')
    horrorCount = genres.count('Horror')
    historyCount = genres.count('History')
    sciencefictionCount = genres.count('Science Fiction')
    mysteryCount = genres.count('Mystery')
    warCount = genres.count('War')
    foreignCount = genres.count('Foreign')
    musicCount = genres.count('Music')
    documentaryCount = genres.count('Documentary')
    westernCount = genres.count('Western')
    tvmovieCount = genres.count('TV Movie')

    genreCountList = [
        animationCount, 
        comedyCount, 
        familyCount, 
        adventureCount, 
        fantasyCount, 
        romanceCount, 
        dramaCount, 
        actionCount, 
        crimeCount, 
        thrillerCount, 
        horrorCount, 
        historyCount, 
        sciencefictionCount, 
        mysteryCount, 
        warCount, 
        foreignCount, 
        musicCount, 
        documentaryCount, 
        westernCount, 
        tvmovieCount
    ]

    cursor.execute("SELECT genre_name FROM movies JOIN ratings ON movies.movie_id = ratings.movie_id JOIN users ON users.user_id = ratings.user_id  JOIN movie_genre ON movies.movie_id = movie_genre.movie_id JOIN genres ON movie_genre.genre_id = genres.genre_id")
    allUsersGenresListDict = cursor.fetchall()
    allUsersGenres = []
    for element in allUsersGenresListDict:
            allUsersGenres.append(element['genre_name'])
    allAnimationCount = allUsersGenres.count('Animation')
    allComedyCount = allUsersGenres.count('Comedy')
    allFamilyCount = allUsersGenres.count('Family')
    allAdventureCount = allUsersGenres.count('Adventure')
    allFantasyCount = allUsersGenres.count('Fantasy')
    allRomanceCount = allUsersGenres.count('Romance')
    allDramaCount = allUsersGenres.count('Drama')
    allActionCount = allUsersGenres.count('Action')
    allCrimeCount = allUsersGenres.count('Crime')
    allThrillerCount = allUsersGenres.count('Thriller')
    allHorrorCount = allUsersGenres.count('Horror')
    allHistoryCount = allUsersGenres.count('History')
    allScienceFictionCount = allUsersGenres.count('Science Fiction')
    allMysteryCount = allUsersGenres.count('Mystery')
    allWarCount = allUsersGenres.count('War')
    allForeignCount = allUsersGenres.count('Foreign')
    allMusicCount = allUsersGenres.count('Music')
    allDocumentaryCount = allUsersGenres.count('Documentary')
    allWesternCount = allUsersGenres.count('Western')
    allTVMovieCount = allUsersGenres.count('TV Movie')

    cursor.execute( #Trying to find total count of users
        "SELECT count(user_id) as count FROM users"
    )

    userCount = cursor.fetchone()['count']

    #Finding averages
    avgAnimationCount = allAnimationCount/userCount
    avgComedyCount = allComedyCount/userCount
    avgFamilyCount = allFamilyCount/userCount
    avgAdventureCount = allAdventureCount/userCount
    avgFantasyCount = allFantasyCount/userCount
    avgRomanceCount = allRomanceCount/userCount
    avgDramaCount = allDramaCount/userCount
    avgActionCount = allActionCount/userCount
    avgCrimeCount = allCrimeCount/userCount
    avgThrillerCount = allThrillerCount/userCount
    avgHorrorCount = allHorrorCount/userCount
    avgHistoryCount = allHistoryCount/userCount
    avgScienceFictionCount = allScienceFictionCount/userCount
    avgMysteryCount = allMysteryCount/userCount
    avgWarCount = allWarCount/userCount
    avgForeignCount = allForeignCount/userCount
    avgMusicCount = allMusicCount/userCount
    avgDocumentaryCount = allDocumentaryCount/userCount
    avgWesternCount = allWesternCount/userCount
    avgTVMovieCount = allTVMovieCount/userCount

    avgGenreCountList = [
        avgAnimationCount,
        avgComedyCount,
        avgFamilyCount,
        avgAdventureCount,
        avgFantasyCount,
        avgRomanceCount,
        avgDramaCount,
        avgActionCount,
        avgCrimeCount,
        avgThrillerCount,
        avgHorrorCount,
        avgHistoryCount,
        avgScienceFictionCount,
        avgMysteryCount,
        avgWarCount,
        avgForeignCount,
        avgMusicCount,
        avgDocumentaryCount,
        avgWesternCount,
        avgTVMovieCount
    ]

    # fig = make_subplots(rows=1, cols=2)

    # fig.add_trace(
    #     go.Bar(name = 'You', x = genreList, y = genreCountList),
    #     row=1, col=1
    # )

    # fig.add_trace(
    #     go.Bar(name = 'Average User', x = genreList, y = avgGenreCountList),
    #     row=1, col=1
    # )

    # fig.add_trace(
    #     go.Bar(name = 'You', x = genreList, y = genreCountList),
    #     row=1, col=2
    # )

    # fig.add_trace(
    #     go.Bar(name = 'Average User', x = genreList, y = avgGenreCountList),
    #     row=1, col=2
    # )

    # fig.update_layout(height=600, width=1400, title_text="Side By Side Subplots")

    fig = go.Figure(data=[
        go.Bar(name = 'You', x = genreList, y = genreCountList),
        go.Bar(name = 'Average User', x = genreList, y = avgGenreCountList)
    ])
    fig.update_layout(barmode = 'group')
    fig.update_layout(height = 600, width = 1400, title_text="Your Genres vs. Average WatchGenie User Genres")
    graphJSON = plotly.io.to_json(fig)
    # graphJSON = json.dumps(data, cls = plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def userBubbleChart():
    user_id = session['id']
    #bubble chart (y-axis: watchgenie avg rating, x-axiz: imdb avg rating, circle size: user rating)
    cursor.execute(
        "SELECT m1.title, t2.rating, avg(r1.rating) as user_base_avg, m1.vote_average as tmdb_avg FROM movies as m1 JOIN (SELECT m2.movie_id, r2.rating FROM movies as m2 JOIN ratings as r2 ON m2.movie_id = r2.movie_id JOIN users ON r2.user_id = users.user_id WHERE users.user_id = %s) as t2 ON m1.movie_id = t2.movie_id JOIN ratings as r1 ON m1.movie_id = r1.movie_id GROUP BY (m1.movie_id)",(user_id)
    )
    bubbleAllList = cursor.fetchall()
    movieTitles = []
    userRatings = []
    avgWGRatings = []
    avgTMDBRatings = []

    for title in bubbleAllList:
        movieTitles.append(title['title'])
        userRatings.append(title['rating'])
        avgWGRatings.append(title['user_base_avg'])
        avgTMDBRatings.append(title['tmdb_avg'])

    d = {'Title' : movieTitles, 'userRating' : userRatings, 'watchGenieRating' : avgWGRatings, 'tmdbRating' : avgTMDBRatings}
    df = pd.DataFrame(data = d)
    fig = px.scatter(df, x = 'watchGenieRating', y = 'tmdbRating', size = 'userRating', hover_name = 'Title', log_x = True, size_max = 60)
    fig.update_layout(height = 600, width = 1400, title_text="Your Bubble Graph", template='plotly_dark').update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    graphJSON = plotly.io.to_json(fig)
    return graphJSON

def genrePopularityGraph(): #NOT FUNCTIONAL
    #Genre Popularity over time
    cursor.execute( #may need to change "month" when dates are added to database
        "SELECT count(rating), genre, rating_date FROM ratings JOIN movies JOIN genres JOIN movie_genre WHERE ratings.movie_id = movies.movie_id AND movies.movie_id = movie_genre.movie_id AND movie_genre.genre_id = genres.genre_id"
    )
    ratingCountPerGenreMonth = cursor.fetchall()
    #may need to group data
    ratingCount = []
    genreCount = []
    monthCount = []
    for genre in ratingCountPerGenreMonth:
        ratingCount.append(genre[0])
        genreCount.append(genre[1])
        dateCount.append(genre[2])
    df3 = {'ratingCount' : ratingCount, 'genre' : genreCount, 'date' : dateCount} 
    fig4 = px.line(df3, x = 'date', y = 'ratingCount', color = 'genre')
    return None

def movie_popularity_over_time(movie_id):
    cursor.execute(
        "SELECT count(rating), rating_date FROM ratings JOIN movies WHERE movie_title = movies.title AND movies.movie_id = ratings.movie_id AND movies.movie_id = %s", (movie_id)
    )
    movieRatingCountAndDate = cursor.fetchall()
    movieRatingCount = []
    ratingDate = []
    for rd in movieRatingCountAndDate:
        movieRatingCount.append(rd['rating'])
        ratingDate.append(rd['rating_date'])
    d = {'Rating Count' : movieRatingCount, 'Date' : ratingDate}
    df = pd.DataFrame(data = d)
    fig = px.line(df, x = 'date', y = 'Rating Count', template='plotly_dark').update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    fig.update_layout(height = 600, width = 1400) #can change dimensions
    fig.update_layout(yaxis = {'visible': False, 'showticklabels': True}) #hide y-axis
    graphJSON = plotly.io.to_json(fig)
    return graphJSON

