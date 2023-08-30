drop database if exists foundation_assessment_ii;
CREATE DATABASE foundation_assessment_ii;
USE foundation_assessment_ii;

CREATE TABLE movie_info (
	Movie_ID INT PRIMARY KEY,
    Movie_Name VARCHAR(150),
    Movie_Length TIME,
    Age_Rating VARCHAR(10)
);
CREATE TABLE screens (
	Screen_ID INT PRIMARY KEY,
    Four_K BOOLEAN
);

CREATE TABLE showings (
	Showing_ID INT PRIMARY KEY,
    Movie_ID INT,
    Screen_ID INT,
    Start_Time DATETIME,
    Available_Seats INT,
    FOREIGN KEY (Movie_ID) REFERENCES movie_info(Movie_ID),
    FOREIGN KEY (Screen_ID) REFERENCES screens(Screen_ID)
);

INSERT INTO movie_info (Movie_ID, Movie_Name, Movie_Length, Age_Rating)
VALUES	(1, "Back to the Future", '01:56:00',  "PG"),
		(2, "Interstellar", '02:49:00', "12A"),
        (3, "Parasite", '02:12:00', "15");

INSERT INTO screens (Screen_ID, Four_K)
VALUES	(1, TRUE),
		(2, TRUE),
        (3, FALSE);

INSERT INTO showings (Showing_ID, Movie_ID, Screen_ID, Start_Time, Available_Seats)
VALUES	(1, 1, 1, '2023-07-13 14:00:00',23),
		(2, 2, 2, '2023-07-12 18:00:00', 2),
        (3, 3, 3, '2023-07-13 20:00:00', 50);

SELECT m.Movie_Name, m.Movie_Length
FROM movie_info m
JOIN showings s ON m.Movie_ID = s.Movie_ID
WHERE s.Start_Time > '2023-07-11 12:00:00' AND s.Available_Seats > 0
ORDER BY s.Start_Time;

SELECT m.Movie_Name
FROM movie_info m
JOIN showings s ON m.Movie_ID = s.Movie_ID
GROUP BY m.Movie_Name
ORDER BY COUNT(*) DESC
LIMIT 1;


