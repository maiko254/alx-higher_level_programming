-- lists all shows contained in the database hbtn_0d_tvshows
-- sort results in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT ts.title, tsg.genre_id
 FROM tv_shows AS ts
   LEFT JOIN tv_show_genres AS tsg
       ON ts.id = tsg.show_id
  ORDER BY ts.title, tsg.genre_id
