-- lists all shows in hbtn_0d_tvshows without a genre linked
-- Each record should display: tv_shows.title, tv_show_genres.genre_id
-- Results must be in ascending order by tv_shows.title and tv_show_genres.genre_id
-- You can only use one SELECT statement

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show
LEFT JOIN tv_shows_genres ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.show is NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
