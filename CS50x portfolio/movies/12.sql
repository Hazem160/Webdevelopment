SELECT title FROM people,stars,movies WHERE people.id = stars.person_id AND stars.movie_id = movies.id
AND name = "Johnny Depp"
INTERSECT
SELECT title FROM people,stars,movies WHERE people.id = stars.person_id AND stars.movie_id = movies.id
AND name = "Helena Bonham Carter";

