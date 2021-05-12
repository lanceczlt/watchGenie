# WatchGenie
WatchGenie is a recommendation website for users to find recommendations for movies to watch. The system is expected to offer relevant recommendations and aims to give users movie recommendations that the users will enjoy. WatchGenie condenses the watch preferences of users using graphs and feedback from users to improve recommendations for other users. 

This web-application’s goal is to not only provide new and interesting movie recommendations, but also to save the user time and energy in the long run. Instead of having to search through long and non-user-specific lists of movies, the user is immediately provided with options that the system finds most fitting. It is also common that users might have a hard time deciding which of the movies they’re interested in watching. This will also facilitate that process and make it easier for the user to move past that problem.

The system is designed to be continuously updated and dynamic so that the recommendations provided for each user can be adjusted as time goes on. By allowing the user to continuously provide feedback on the recommended movies that we provide, we will be able to further improve the user experience and accuracy of our recommendations. Not only that, but we also allow users to adjust or remove their previous review/feedback in case their opinion of any movie changes. These features will allow the system and algorithm to keep up with the user changes frequently and avoid having a static, shallow understanding of each user.

Additionally, it is scientifically proven that providing personalized products designated towards the user themselves promotes user attention, interest, and trust. Allowing users to know that our recommendations are made specifically for them will promote the usage and popularity of our software. The system will also provide interesting data informatics about the user’s own data in order to demonstrate the personalization aspect.

# Installation manual 

## Initial Installations:
### Initial Installations/Dependencies
Using any python IDE (preferably, VSCode), unzip the files and open the watchGenie folder as the directory. Before, we can get started, make sure to install these dependencies through pip:
numpy==1.19.2
scipy==1.5.2
plotly==4.14.3
requests==2.24.0
pandas==1.1.3
Flask==1.1.2
Flask_Session==0.3.2
PyMySQL==1.0.2
python_dateutil==2.8.1

### Database Backend
Please install a mySQL server and an associating GUI (phpmyadmin or workbench) to initialize the local database backend. Create a localhost server and initialize a database schema called watch genie:
‘create schema watchgenie’
Set that schema as the default (‘Set As Default Schema’ once you right click the database) in order for the SQL queries to work as directed. Once completed, open ‘database_connection.py’ in ‘watchgenie/website/database_connection’  and under def connect(), change the user, password, and host to the current one that’s holding watchgenie. (also change database if you set the name to something else)

### Data Population
Before our webapp can be run, it must be populated with data. To do so, go to the directory ‘watchgenie/database_sql’. In this folder, there are multiple large SQL files that will create and populate the database.
The first set of files to be run is : movies.sql, actors.sql, tags.sql, genres.sql, and users.sql. These must be populated first because they are the tables that second set of files depends on (constraints limitations)
The second set of files to run is: links.sql, movie_actor.sql, movie_genre.sql, movie_tag.sql, ratings.sql, and user_rec.sql. 
Since the data is so large, some inputs might not be able to be inserted (if movie_id does not exist, and so it is inputted as ‘INSERT IGNORE INTO’. 
The last set of files to run is: triggers.sql. Which simply holds the triggers of our project. Once completed, the initial database is completely set up.

### Running the web-app
	All that is left now is to run main.py. Which will initialize the application and provide a local address to access the website. Simply sign up, login, and provide at least 5 movie recommendations.


# Class Definitions/Explainations
watchgenie/ main.py
	This class is meant as a quick way for the user to easily start the application. All it does is creates the flask app and runs it in debug, local mode. 

watchgenie/website/
	This folder stores the main components of this application, from the html, css, and js to the actual flask code and recommendation/visualize code that combines it all together.

watchgenie/database_sql
	As previously mentioned, this folder contains all the SQL necessary to create and populate our local database.

watchgenie/website/static
	This folder contains all the CSS/JS/ and IMAGES that are used locally for our project.

watchgenie/website/templates
	This folder contains all the HTML web pages that our application has. All html files are labeled in a way that makes it obvious which file contains which webpage.

watchgenie/website/db_connection.py
	This python file holds PyMySQL cursor and connection initializers. It is called throughout every other python file in order to allow the system to interact with the database to query or insert information and data. It also contains a function called ‘def get_movie_image’, which calls from the TMDB API. This is the only API data pull we use in our application -- every other information is queried from our database. We simply retrieve a movie poster png (URL link) for the list of movies that we show the user.

watchgenie/website/auth.py
	This python file holds the flask Blueprints and interactions with the user when it comes to signing up, logging in, and logging out. The application uses session to store the current user information of the LOGGED IN user. This information is stored locally for now. The session information is used as parameters for many queries throughout the application.

watchgenie/website/views.py
	This python file holds every other flask Blueprint function that renders the HTML files and provides it with parameters queried from the database and unique to the user. 

watchgenie/website/recommend.py
	This python file holds the primary movie recommendation algorithm. The function get_movie_recommendation_content is called provided the user’s unique user_id. The user’s previous rating and all associated movies are queried from the database to be analyzed in our algorithm. The algorithm creates a vector matrix using the content of each movie and the entire user reviews queried from our database. The user’s own reviews are then calculated in order to get the most similar/correlated movies and users (with similar reviews). These are then combined in order to return a list of movie_id’s of 30 movie recommendations.

watchgenie/website/visualize.py
	This python file holds the code to generate the visualizations specific to the user. It queries the database to get information about the user and the average user in order to create graphs to compare the two. This is done using plotly, a python extension that allows for easy creation of interactive and downloadable graphs.
