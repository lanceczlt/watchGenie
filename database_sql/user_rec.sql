CREATE TABLE IF NOT EXISTS `cur_rec` (
  `user_id` INTEGER NOT NULL,
  `movie_id` INTEGER NOT NULL,
  `have_watched` BOOLEAN NOT NULL,
  PRIMARY KEY (`user_id`, `movie_id`),
  FOREIGN KEY (`movie_id`) REFERENCES movies(`movie_id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`user_id`)
);

CREATE TABLE IF NOT EXISTS `prev_rec` (
  `user_id` INTEGER NOT NULL,
  `movie_id` INTEGER NOT NULL,
  `have_watched` BOOLEAN NOT NULL,
  PRIMARY KEY (`user_id`, `movie_id`),
  FOREIGN KEY (`movie_id`) REFERENCES movies(`movie_id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`user_id`)
);