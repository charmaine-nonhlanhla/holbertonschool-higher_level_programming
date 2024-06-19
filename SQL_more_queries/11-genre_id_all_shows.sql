-- Query to list all shows with associated genre IDs or NULL if no genre is linked

SELECT tv_shows.title, IFNULL(tv_show_genres.genre_id, 'NULL') AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, genre_id ASC;

