SELECT DISTINCT name FROM ratings,directors,people WHERE ratings.movie_id = directors.movie_id
AND directors.person_id= people.id AND rating >= 9.0;