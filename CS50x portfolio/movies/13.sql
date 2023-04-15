SELECT name FROM people WHERE id IN
(SELECT person_id from stars WHERE person_id!= (SELECT id FROM people WHERE name = "Kevin Bacon")
    AND movie_id IN
(SELECT movies.id FROM people,stars,movies WHERE people.id= stars.person_id
AND stars.movie_id = movies.id
AND name = "Kevin Bacon"
INTERSECT
SELECT movies.id FROM people,stars,movies WHERE people.id= stars.person_id
AND stars.movie_id = movies.id AND birth=1958));
