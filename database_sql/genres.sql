CREATE TABLE IF NOT EXISTS genres(
   genre_id   INTEGER  NOT NULL PRIMARY KEY 
  ,genre_name VARCHAR(15) NOT NULL
);

INSERT INTO genres(genre_id,genre_name) VALUES
 (16,'Animation')
,(35,'Comedy')
,(10751,'Family')
,(12,'Adventure')
,(14,'Fantasy')
,(10749,'Romance')
,(18,'Drama')
,(28,'Action')
,(80,'Crime')
,(53,'Thriller')
,(27,'Horror')
,(36,'History')
,(878,'Science Fiction')
,(9648,'Mystery')
,(10752,'War')
,(10769,'Foreign')
,(10402,'Music')
,(99,'Documentary')
,(37,'Western')
,(10770,'TV Movie');