#!/usr/bin/env python
# coding: utf-8

import sqlalchemy

import pandas as pd

from pprint import pprint

engine = sqlalchemy.create_engine('postgresql://kat:kat2602@localhost:5432/musicial_studio')
# engine

connection = engine.connect()

# connection.execute("""INSERT INTO actors(id, name)
#            VALUES
#            (1, 'Shufutinskiy');
#  """)

# connection.execute("""INSERT INTO actors(id, name)
#            VALUES
#            (2, 'Krug'),
#            (3, 'Allegrova'),
#            (4, 'Agata Kristi'),
#            (5, 'Zemfira'),
#            (6, 'Pugacheva'),
#            (7, 'Kirkorov'),
#            (8, 'Lolita');
#
#  """)

# sel_a = connection.execute("""SELECT * FROM actors;
# """).fetchmany(10)
# pprint(sel_a)


# pd.DataFrame(sel)
# pprint(sel)

#
# connection.execute("""INSERT INTO genre(id, name)
#            VALUES
#            (1, 'Шансон'),
#            (2, 'Попса'),
#            (3, 'Рок'),
#            (4, 'Рэп'),
#            (5, 'Инструментальное');
#  """)

# sel_g = connection.execute("""SELECT * FROM genre;
# """).fetchmany(10)
# pprint(sel_g)

# connection.execute("""INSERT INTO albums(id, name, year)
#            VALUES
#            (1, 'Shans', 2018),
#            (2, 'Cold', 2019),
#            (3, 'Zhara', 2005),
#            (4, 'One', 2006),
#            (5, 'Opel', 2018),
#            (6, 'Kaktus', 2020),
#            (7, 'Nebo', 2018),
#            (8, 'Djs', 2017);
#
#  """)
#
# sel_al = connection.execute("""SELECT * FROM albums;
# """).fetchmany(10)
# pprint(sel_al)

# connection.execute("""INSERT INTO tracks(id, name, duration, albums_id)
#            VALUES
#            (1, 'Ne esh s nozha', 3.30, 1),
#            (2, 'Posvyashenie roditelyam', 5.00, 3),
#            (3, 'Na titanike', 4.30, 8),
#            (4, 'Skazochnya taiga', 2.35, 4),
#            (5, 'Butylka vina', 3.25, 1),
#            (6, 'Dyadya Pasha', 3.30, 1),
#            (7, 'Sneg', 2.55, 7),
#            (8, 'Arlekino', 3.45, 6),
#            (9, 'Do svidaniya', 4.20, 5),
#            (10, 'Studentka', 4.10, 2),
#            (11, 'Romashki', 4.05, 5),
#            (12, 'Piter Moskva', 2.50, 1),
#            (13, 'Mosty', 3.15, 1),
#            (14, 'Zahodite v moy dom', 3.05, 2),
#            (15, 'Tak zhe kak vse', 3.40, 6),
#            (16, 'Kover vertolet', 3.50, 4);
#
#  """)
#
# sel_tr = connection.execute("""SELECT * FROM tracks;
# """).fetchmany(10)
# pprint(sel_tr)

# connection.execute("""INSERT INTO collection(id, name, year)
#            VALUES
#            (1, 'One', 2019),
#            (2, 'Two', 2018),
#            (3, 'Three', 2006),
#            (4, 'Four', 2011),
#            (5, 'Five', 2020),
#            (6, 'Six', 2017),
#            (7, 'Seven', 2019),
#            (8, 'Eight', 2003);
#  """)

# sel_col = connection.execute("""SELECT * FROM collection;
# """).fetchmany(10)
# pprint(sel_col)

# connection.execute("""INSERT INTO trackscollection(tracks_id, collection_id)
#            VALUES
#            (1, 1),
#            (2, 8),
#            (3, 5),
#            (4, 1),
#            (5, 3),
#            (6, 4),
#            (7, 6),
#            (8, 7),
#            (9, 8),
#            (10, 6),
#            (11, 4),
#            (12, 2),
#            (13, 1),
#            (14, 3),
#            (15, 5),
#            (16, 7);
#  """)

# sel_tc = connection.execute("""SELECT * FROM trackscollection;
# # """).fetchmany(10)
# # pprint(sel_tc)

# connection.execute("""INSERT INTO genreactors(genre_id, actors_id)
#            VALUES
#            (1, 1),
#            (2, 6),
#            (3, 4),
#            (4, 8),
#            (5, 7);
#  """)
#
# sel_ga = connection.execute("""SELECT * FROM genreactors;
#  """).fetchmany(10)
# pprint(sel_ga)

# connection.execute("""INSERT INTO actorsalbums(actors_id, albums_id)
#            VALUES
#            (1, 8),
#            (2, 7),
#            (3, 6),
#            (4, 1),
#            (5, 2),
#            (6, 4),
#            (7, 3),
#            (8, 5);
#  """)
#
# sel_aa = connection.execute("""SELECT * FROM actorsalbums;
#  """).fetchmany(10)
# pprint(sel_aa)

# connection.execute("""INSERT INTO tracks(id, name, duration, albums_id)
#            VALUES
#            (17, 'My love', 3.20, 1),
#            (18, 'My family', 3.50, 3);
#  """)

# connection.execute("""UPDATE tracks
#            SET duration = 320
#            WHERE id = 1;
#  """)
#
# connection.execute("""UPDATE tracks
#            SET duration = 120
#            WHERE id = 2;
#  """)
# connection.execute("""UPDATE tracks
#            SET duration = 240
#            WHERE id = 3;
#  """)
# connection.execute("""UPDATE tracks
#            SET duration = 190
#            WHERE id = 4;
#  """)
# connection.execute("""UPDATE tracks
#            SET duration = 410
#            WHERE id = 5;
#  """)
# connection.execute("""UPDATE tracks
#            SET duration = 220
#            WHERE id = 6;
#  """)
# connection.execute("""UPDATE tracks
#            SET duration = 205
#            WHERE id = 7;
#  """)
# connection.execute("""UPDATE tracks
#            SET duration = 130
#            WHERE id = 8;
#  """)
# connection.execute("""UPDATE tracks
#            SET duration = 120
#            WHERE id = 9;
#  """)
# connection.execute("""UPDATE tracks
#            SET duration = 250
#            WHERE id = 10;
#  """)
# connection.execute("""UPDATE tracks
#            SET duration = 120
#            WHERE id = 11;
#  """)
# connection.execute("""UPDATE tracks
#            SET duration = 270
#            WHERE id = 12;
#  """)
# connection.execute("""UPDATE tracks
#            SET duration = 200
#            WHERE id = 13;
#  """)
# connection.execute("""UPDATE tracks
#            SET duration = 140
#            WHERE id = 14;
#  """)
# connection.execute("""UPDATE tracks
#            SET duration = 2050
#            WHERE id = 15;
#  """)
# connection.execute("""UPDATE tracks
#            SET duration = 120
#            WHERE id = 16;
#  """)
# connection.execute("""UPDATE tracks
#            SET duration = 140
#            WHERE id = 17;
#  """)
# connection.execute("""UPDATE tracks
#            SET duration = 140
#            WHERE id = 18;
#  """)
#
# sel_tr = connection.execute("""SELECT * FROM tracks;
# """).fetchmany(20)
# pprint(sel_tr)

# connection.execute("""INSERT INTO actorsalbums(actors_id, albums_id)
#            VALUES
#            (1, 7),
#            (2, 8),
#            (3, 8),
#            (4, 7),
#            (8, 7);
#  """)
#
# sel_aa = connection.execute("""SELECT * FROM actorsalbums;
#  """).fetchall
# pprint(sel_aa)

# connection.execute("""INSERT INTO albums(id, name, year)
#            VALUES
#            (9, 'Piter', 2002),
#            (10, 'Moskva', 2021);
#  """)

# connection.execute("""INSERT INTO tracks(id, name, duration, albums_id)
#            VALUES
#            (19, 'Piter-Moskva', 150, 9),
#            (20, 'Studentka', 220, 10),
#            (21, 'Forest', 135, 10);
#  """)
#
# sel_tr = connection.execute("""SELECT * FROM tracks;
# """).fetchall
# pprint(sel_tr)



