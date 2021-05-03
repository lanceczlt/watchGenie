CREATE TABLE IF NOT EXISTS user_rec(
   user_id     INTEGER  NOT NULL
  ,movie_id    INTEGER  NOT NULL   
  ,have_watched BOOLEAN NOT NULL
  ,current_rec BOOLEAN NOT NULL
  ,PRIMARY KEY(user_id, movie_id)
  ,FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
  ,FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);