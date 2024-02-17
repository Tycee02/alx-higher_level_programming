-- import the db dump from hbtn_0d_tvshows
-- lists all shows contained in hbtn_0d_tvshows that have at least one genre b linkde
-- Each record should display: tv_shows.title - tv_show_genres.genre_id

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
