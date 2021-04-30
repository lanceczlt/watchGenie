import plotly.express as px

visualize = Blueprint('visualize', __name__)

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
        
        
        animationCount = genres.count('Animation'),
        comedyCount = genres.count('Comedy'),
        familyCount = genres.count('Family'),
        adventureCount = genres.count('Adventure'),
        fantasyCount = genres.count('Fantasy'),
        romanceCount = genres.count('Romance'),
        dramaCount = genres.count('Drama'),
        actionCount = genres.count('Action'),
        crimeCount = genres.count('Crime'),
        thrillerCount = genres.count('Thriller'),
        horrorCount = genres.count('Horror'),
        historyCount = genres.count('History'),
        sciencefictionCount = genres.count('Science Fiction'),
        mysteryCount = genres.count('Mystery'),
        warCount = genres.count('War'),
        foreignCount = genres.count('Foreign'),
        musicCount = genres.count('Music'),
        documentaryCount = genres.count('Documentary'),
        westernCount = genres.count('Western'),
        tvmovieCount = genres.count('TV Movie'),

        genreCountList = [animationCount, comedyCount, familyCount, adventureCount, fantasyCount, romanceCount, dramaCount, actionCount, crimeCount, thrillerCount, horrorCount, historyCount, sciencefictionCount, mysteryCount, warCount, foreignCount, musicCount, documentaryCount, westernCount, tvmovieCount

        ]

        d = {'Genre': genreList, 'Count': genreCountList}
        df = pd.DataFrame(data=d)

        fig = px.pie(df, values = 'Count', names = 'Genre')
        fig.show()

    else:
        return redirect(url_for('auth.login'))

