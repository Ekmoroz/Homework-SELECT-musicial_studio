#!/usr/bin/env python
# coding: utf-8

import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://kat:kat2602@localhost:5432/musicial_studio')
connection = engine.connect()

# 1
one = connection.execute("""SELECT name, year FROM albums
WHERE year = 2018;
""").fetchall()
print(one)

# 2
two = connection.execute("""SELECT name, duration FROM tracks
ORDER BY duration DESC
LIMIT 1;
""").fetchall()
print(two)

# 3
three = connection.execute("""SELECT name FROM tracks
WHERE duration >= 210;
""").fetchall()
print(three)

# 4
four = connection.execute("""SELECT name FROM collection
WHERE year BETWEEN 2018 AND 2020;
""").fetchall()
print(four)

# 5
five = connection.execute("""SELECT name FROM actors
WHERE name NOT LIKE '%% %%';
""").fetchall()
print(five)

# 6
six = connection.execute("""SELECT name FROM tracks
WHERE name LIKE '%%My%%';
""").fetchall()
print(six)