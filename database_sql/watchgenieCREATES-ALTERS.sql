CREATE TABLE IF NOT EXISTS `person` (
  `person_id` INTEGER PRIMARY KEY NOT NULL,
  `name` VARCHAR(30) NOT NULL,
  `gender` VARCHAR(6) NOT NULL
);

CREATE TABLE IF NOT EXISTS `users` (
  `user_id` INTEGER NOT NULL,
  `person_id` INTEGER NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `password` VARCHAR(50) NOT NULL,
  `age` INTEGER NOT NULL,
  PRIMARY KEY (`user_id`, `person_id`)
);

CREATE TABLE IF NOT EXISTS `prequel` (
  `movie_id` INTEGER NOT NULL,
  `prequel_id` INTEGER NOT NULL,
  PRIMARY KEY (`movie_id`, `prequel_id`)
);

CREATE TABLE IF NOT EXISTS `sequel` (
  `movie_id` INTEGER NOT NULL,
  `sequel_id` INTEGER NOT NULL,
  PRIMARY KEY (`movie_id`, `sequel_id`)
);

CREATE TABLE IF NOT EXISTS `tags` (
  `tag_id` INTEGER PRIMARY KEY NOT NULL,
  `tag_name` VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS `movie_tag` (
  `movie_id` INTEGER NOT NULL,
  `tag_id` INTEGER NOT NULL,
  PRIMARY KEY (`movie_id`, `tag_id`)
);

CREATE TABLE IF NOT EXISTS `movies` (
  `movie_id` INTEGER PRIMARY KEY NOT NULL,
  `title` VARCHAR(120) NOT NULL,
  `overview` VARCHAR(1000) NOT NULL,
  `budget` INTEGER NOT NULL,
  `popularity` INTEGER NOT NULL,
  `release_date` DATE NOT NULL,
  `revenue` INTEGER NOT NULL,
  `duration` INTEGER NOT NULL,
  `vote_average` INTEGER NOT NULL,
  `vote_count` INTEGER NOT NULL,
  FULLTEXT KEY(title)
);

CREATE TABLE IF NOT EXISTS `actors` (
  `actor_id` INTEGER NOT NULL,
  `person_id` INTEGER NOT NULL,
  PRIMARY KEY (`actor_id`, `person_id`)
);

CREATE TABLE IF NOT EXISTS `genres` (
  `genre_id` INTEGER PRIMARY KEY NOT NULL,
  `genre_name` VARCHAR(15) NOT NULL
);

CREATE TABLE IF NOT EXISTS `links` (
  `movie_id` INTEGER PRIMARY KEY NOT NULL,
  `imdb_id` INTEGER NOT NULL,
  `tmdb_id` INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS `movie_actor` (
  `movie_id` INTEGER NOT NULL,
  `actor_id` INTEGER NOT NULL,
  `role` VARCHAR(400) NOT NULL,
  PRIMARY KEY (`movie_id`, `actor_id`)
);

CREATE TABLE IF NOT EXISTS `movie_genre` (
  `movie_id` INTEGER NOT NULL,
  `genre_id` INTEGER NOT NULL,
  PRIMARY KEY (`movie_id`, `genre_id`)
);

CREATE TABLE IF NOT EXISTS `ratings` (
  `user_id` INTEGER NOT NULL,
  `movie_id` INTEGER NOT NULL,
  `rating` INTEGER NOT NULL,
  `rating_date` DATETIME NOT NULL,
  PRIMARY KEY (`user_id`, `movie_id`)
);

CREATE TABLE IF NOT EXISTS `cur_rec` (
  `user_id` INTEGER NOT NULL,
  `movie_id` INTEGER NOT NULL,
  `have_watched` BOOLEAN NOT NULL,
  PRIMARY KEY (`user_id`, `movie_id`)
);

CREATE TABLE IF NOT EXISTS `prev_rec` (
  `user_id` INTEGER NOT NULL,
  `movie_id` INTEGER NOT NULL,
  `have_watched` BOOLEAN NOT NULL,
  PRIMARY KEY (`user_id`, `movie_id`)
);

ALTER TABLE `links` ADD FOREIGN KEY (`movie_id`) REFERENCES `movies` (`movie_id`) ON DELETE CASCADE;

ALTER TABLE `movie_actor` ADD FOREIGN KEY (`movie_id`) REFERENCES `movies` (`movie_id`) ON DELETE CASCADE;

ALTER TABLE `movie_actor` ADD FOREIGN KEY (`actor_id`) REFERENCES `actors` (`actor_id`) ON DELETE CASCADE;

ALTER TABLE `movie_genre` ADD FOREIGN KEY (`movie_id`) REFERENCES `movies` (`movie_id`) ON DELETE CASCADE;

ALTER TABLE `movie_genre` ADD FOREIGN KEY (`genre_id`) REFERENCES `genres` (`genre_id`) ON DELETE CASCADE;

ALTER TABLE `ratings` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE;

ALTER TABLE `ratings` ADD FOREIGN KEY (`movie_id`) REFERENCES `movies` (`movie_id`) ON DELETE CASCADE;

ALTER TABLE `cur_rec` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE;

ALTER TABLE `cur_rec` ADD FOREIGN KEY (`movie_id`) REFERENCES `movies` (`movie_id`) ON DELETE CASCADE;

ALTER TABLE `prev_rec` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE;

ALTER TABLE `prev_rec` ADD FOREIGN KEY (`movie_id`) REFERENCES `movies` (`movie_id`) ON DELETE CASCADE;

ALTER TABLE `movies` ADD FOREIGN KEY (`movie_id`) REFERENCES `movies` (`title`) ON DELETE CASCADE;

ALTER TABLE `person` ADD FOREIGN KEY (`person_id`) REFERENCES `users` (`person_id`) ON DELETE CASCADE;

ALTER TABLE `person` ADD FOREIGN KEY (`person_id`) REFERENCES `actors` (`person_id`) ON DELETE CASCADE;

ALTER TABLE `movie_actor` ADD FOREIGN KEY (`role`) REFERENCES `movie_actor` (`movie_id`) ON DELETE CASCADE;

ALTER TABLE `movies` ADD FOREIGN KEY (`movie_id`) REFERENCES `sequel` (`movie_id`) ON DELETE CASCADE;

ALTER TABLE `movies` ADD FOREIGN KEY (`movie_id`) REFERENCES `sequel` (`sequel_id`) ON DELETE CASCADE;

ALTER TABLE `movies` ADD FOREIGN KEY (`movie_id`) REFERENCES `prequel` (`movie_id`) ON DELETE CASCADE;

ALTER TABLE `movies` ADD FOREIGN KEY (`movie_id`) REFERENCES `prequel` (`prequel_id`) ON DELETE CASCADE;

ALTER TABLE `movie_tag` ADD FOREIGN KEY (`movie_id`) REFERENCES `movies` (`movie_id`) ON DELETE CASCADE;

ALTER TABLE `movie_tag` ADD FOREIGN KEY (`tag_id`) REFERENCES `tags` (`tag_id`) ON DELETE CASCADE;

