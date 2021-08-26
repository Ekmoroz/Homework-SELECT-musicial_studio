#!/usr/bin/env python
# coding: utf-8

import sqlalchemy

import pandas as pd

from pprint import pprint

engine = sqlalchemy.create_engine('postgresql://kat:kat2602@localhost:5432/musicial_studio')

connection = engine.connect()

# 1/количество исполнителей в каждом жанре
one = connection.execute("""
SELECT genre.name, COUNT (actors.name)
FROM genre
JOIN genreactors ON genre.id = genreactors.genre_id
JOIN actors ON genreactors.actors_id = actors.id
GROUP BY genre.name
ORDER BY COUNT(actors.name) DESC;
""").fetchall()
# pprint(one)

# 2/количество треков, вошедших в альбомы 2019-2020 годов;
two = connection.execute("""
SELECT COUNT(tracks.id)
FROM albums
JOIN tracks ON albums.id = tracks.albums_id
WHERE year BETWEEN 2019 AND 2020;
""").fetchall()
# pprint(two)

# 3/средняя продолжительность треков по каждому альбому;
three = connection.execute("""
SELECT al.name, AVG(tr.duration)
FROM albums al
LEFT JOIN tracks tr ON al.id = tr.albums_id
GROUP BY al.name
ORDER BY AVG(tr.duration);
""").fetchall()
# pprint(three)

# 4/все исполнители, которые не выпустили альбомы в 2020 году;
four = connection.execute("""
SELECT DISTINCT ac.name
FROM actors ac
JOIN actorsalbums aa ON aa.actors_id = ac.id
JOIN albums al ON aa.albums_id = al.id
WHERE NOT al.year = 2020;
""").fetchall()
# pprint(four)

# 5/названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
five = connection.execute("""
SELECT DISTINCT col.name
FROM collection col
JOIN trackscollection tc ON col.id = tc.collection_id
JOIN tracks tr ON tc.tracks_id = tr.id
JOIN albums al ON tr.albums_id = al.id
JOIN actorsalbums aa ON al.id = aa.albums_id
JOIN actors ac ON aa.actors_id = ac.id
WHERE ac.name LIKE '%%Krug%%';
""").fetchall()
# pprint(five)

# 6/название альбомов, в которых присутствуют исполнители более 1 жанра;
six = connection.execute("""
SELECT al.name
FROM genre g
JOIN genreactors ga ON g.id = ga.genre_id
JOIN actors ac ON ga.actors_id = ac.id
JOIN actorsalbums aa ON ac.id = aa.actors_id
JOIN albums al ON aa.albums_id = al.id
GROUP BY al.name
HAVING COUNT(DISTINCT g.name) > 1;
""").fetchall()
# pprint(six)

# 7/наименование треков, которые не входят в сборники;
seven = connection.execute("""
SELECT tr.name
FROM tracks tr
LEFT JOIN trackscollection tc ON tr.id = tc.tracks_id
WHERE tc.tracks_id IS NULL;
""").fetchall()
# pprint(seven)

# 8/исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
eight = connection.execute("""
SELECT DISTINCT ac.name
FROM actors ac
LEFT JOIN actorsalbums aa ON ac.id = aa.actors_id
LEFT JOIN albums al ON aa.albums_id = al.id
LEFT JOIN tracks tr ON al.id = tr.albums_id
WHERE tr.duration = (
SELECT MIN(duration) FROM tracks);
""").fetchall()
# pprint(eight)

# 9/название альбомов, содержащих наименьшее количество треков.
nine = connection.execute("""
SELECT al.name, COUNT(tr.id)
FROM albums al
LEFT JOIN tracks tr ON al.id = tr.albums_id
GROUP BY al.name
HAVING COUNT(tr.id) = 1;
""").fetchall()
# pprint(nine)

# 9/название альбомов, содержащих наименьшее количество треков.
nine = connection.execute("""
SELECT al.name
FROM albums al
LEFT JOIN tracks tr ON al.id = tr.albums_id
WHERE tr.albums_id in(
    SELECT albums_id from tracks
    GROUP BY albums_id
    HAVING COUNT(id) = (
        SELECT COUNT(id) from tracks
        GROUP BY albums_id
        ORDER BY COUNT
        LIMIT 1
        ));
""").fetchall()
# pprint(nine)