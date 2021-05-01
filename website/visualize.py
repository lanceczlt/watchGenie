from flask import Blueprint, render_template, request, flash, jsonify, session, redirect, url_for
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from db_connection import connect


visualize = Blueprint('visualize', __name__)
connect, cursor = connect()

@visualize.route('/visualize', methods=['GET', 'POST'])
def home():
    if 'username' in session:
        return render_template("visualize.html")


    if request.method == 'GET':
        cursor.execute(
            "SELECT genres FROM moviegenie.movies JOIN moviegenie.ratings JOIN moviegenie.users WHERE moviegenie.movies.movie_id = moviegenie.ratings.movie_id AND moviegenie.users.user_id = moviegenie.ratings.user_id"
        )
        genres = cursor.fetchall()
        
        genreList = ['Animation', 'Comedy', 'Family', 'Adventure', 'Fantasy', 'Romance', 'Drama', 'Action', 'Crime', 'Thriller', 'Horror', 'History', 'Science Fiction', 'Mystery', 'War', 'Foreign', 'Music', 'Documentary', 'Western', 'TV Movie']
        
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

        genreCountList = [animationCount, comedyCount, familyCount, adventureCount, fantasyCount, romanceCount, dramaCount, actionCount, crimeCount, thrillerCount, horrorCount, historyCount, sciencefictionCount, mysteryCount, warCount, foreignCount, musicCount, documentaryCount, westernCount, tvmovieCount

        ]

        #pie chart
        d1 = {'Genre': genreList, 'Count': genreCountList}
        df1 = pd.DataFrame(data=d1)
        fig1 = px.pie(df1, values = 'Count', names = 'Genre')
        fig1.show()

        #bar chart comparison
        cursor.execute( #Trying to take in all genres of movie reviews of all users
            "SELECT genres FROM moviegenie.movies JOIN moviegenie.ratings JOIN moviegenie.users WHERE moviegenie.movies.movie_id = moviegenie.ratings.movie_id"
        )
        allUsersGenres = cursor.fetchall()

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
            "SELECT count(user_id) FROM moviegenie.users"
        )
        userCount = cursor.fetchone()[0]
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

        fig2 = go.Figure(
            data=[
                go.Bar(name = 'You', x = genreList, y = genreCountList),
                go.Bar(name = 'Average User', x = genreList, y = avgGenreCountList)
            ]
        )
        fig2.update_layout(barmode = 'group')
        fig2.show()

        #bubble chart (y-axis: watchgenie avg rating, x-axiz: imdb avg rating, circle size: user rating)
        cursor.execute(
            "SELECT title, rating FROM moviegenie.movies JOIN moviegenie.ratings JOIN moviegenie.users WHERE moviegenie.users.user_id = moviegenie.ratings.user_id AND moviegenie.movies.movie_id = moviegenie.ratings.movie_id"
        )
        movieTitles_userRatings = cursor.fetchall()

        movieTitles = []
        userRatings = []
        for title in movieTitles_userRatings:
            movieTitles.append(title[0])
            userRatings.append(title[1])

        cursor.execute(
            "SELECT avg(rating) FROM moviegenie.ratings JOIN moviegenie.users WHERE moviegenie.users.user_id = moviegenie.ratings.user_id"
        )
        avgWGRatings = cursor.fetchall()

        cursor.execute(
            "SELECT vote_average FROM moviegenie.movies JOIN moviegenie.users JOIN moviegenie.ratings WHERE moviegenie.users.user_id = moviegenie.ratings.user_id AND moviegenie.movies.movie_id = moviegenie.ratings.movie_id"
        )
        avgTMDBRatings = cursor.fetchall()

        df2 = {'Title' : movieTitles, 'userRating' : userRatings, 'watchGenieRating' : avgWGRatings, 'tmdbRating' : avgTMDBRatings}

        fig3 = px.scatter(df2, x = 'watchGenieRating', y = 'tmdbRating', size = 'userRating', hover_name = 'Title', log_x = True, size_max = 60)
        fig3.show()

        #Genre Popularity over time
        cursor.execute( #may need to change "month" when dates are added to database
            "SELECT count(rating), genre, rating_date FROM moviegenie.ratings JOIN moviegenie.movies JOIN moviegenie.genres JOIN moviegenie.movie_genre WHERE moviegenie.ratings.movie_id = moviegenie.movies.movie_id AND moviegenie.movies.movie_id = moviegenie.movie_genre.movie_id AND moviegenie.movie_genre.genre_id = moviegenie.genres.genre_id"
        )
        ratingCountPerGenreMonth = cursor.fetchall()
        #may need to group data
        ratingCount = []
        genreCount = []
        monthCount = []
        dateCount = []
        for genre in ratingCountPerGenreMonth:
            ratingCount.append(genre[0])
            genreCount.append(genre[1])
            dateCount.append(genre[2])
        df3 = {'ratingCount' : ratingCount, 'genre' : genreCount, 'date' : dateCount} 
        fig4 = px.line(df3, x = 'date', y = 'ratingCount', color = 'genre')

        def movie_popularityOT(movie_title):
            cursor.execute(
                "SELECT count(rating), rating_date FROM moviegenie.ratings JOIN moviegenie.movies WHERE movie_title = moviegenie.movies.title AND moviegenie.movies.movie_id = moviegenie.ratings.movie_id"
            )
            movieRatingCountAndDate = cursor.fetchall()
            movieRatingCount = []
            ratingDate = []
            for rd in movieRatingCountAndDate:
                movieRatingCount.append(rd[0])
                ratingDate.append(rd[1])
            df4 = {'ratingCount' : movieRatingCount, 'date' : ratingDate}
            fig5 = px.line(df4, x = 'date', y = 'ratingCount')
            return fig5.show()

    else:
        return redirect(url_for('auth.login'))

