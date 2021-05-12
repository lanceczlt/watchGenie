
DELIMITER $$
CREATE TRIGGER keepRecHistory
BEFORE DELETE ON cur_rec
FOR EACH ROW
BEGIN
    INSERT INTO prev_rec VALUES (old.user_id, old.movie_id);
END;
$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER just_watched
AFTER INSERT ON ratings 
FOR EACH ROW
BEGIN
       DECLARE movie_exists Boolean;
       -- Check reccomendation table
       SELECT 1
       INTO @movie_exists
       FROM cur_rec
       WHERE cur_rec.user_id = NEW.user_id AND cur_rec.movie_id = NEW.movie_id;
       
       IF @movie_exists = 1
       THEN
           UPDATE cur_rec
           SET have_watched = '1'
           WHERE cur_rec.user_id = NEW.user_id AND cur_rec.movie_id = NEW.movie_id;
        END IF;
END;
$$
DELIMITER ;
