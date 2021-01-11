# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = """ CREATE TABLE songplays (songplay_id int, start_time int, user_id int, level char, song_id int, artist_id int, session_id int, location text, user_agent text, PRIMARY KEY ( user_id, artist_id))
"""

user_table_create = """ CREATE TABLE users (user_id int, first_name text, last_name text, gender char, level char, PRIMARY KEY ( user_id) )
"""

song_table_create = """ CREATE TABLE songs (song_id text , title text, artist_id text, year int, duration int, PRIMARY KEY ( song_id, artist_id ) )
"""

artist_table_create = """ CREATE TABLE artists (artist_id text, name text, location text, latitude char, longitude char, PRIMARY KEY ( artist_id ) )
"""

time_table_create = """ CREATE TABLE time (start_time int, hour int , day char, week char, month char,  weekday char, PRIMARY KEY ( start_time ) )
"""

# INSERT RECORDS

songplay_table_insert = """INSERT INTO songplay (songplay_id, start_time, user_id, level, song_id, artist_id,  session_id, location, user_agent) VALUES( %, %, %, %, %, %, %, %, %);"""

user_table_insert = """INSERT INTO users ( user_id, first_name, last_name, gender, level) VALUES( %, %, %, %, %); """

song_table_insert = """INSERT INTO songs (song_id, title, artist_id, year, duration)  VALUES( %, %, %, %, %); """

artist_table_insert = """INSERT INTO artists(artist_id, name, location, latitude, longitude)  VALUES( %, %, %, %, %); """


time_table_insert = """INSERT INTO time (start_time, hour, day, week, month, weekday)  VALUES( %, %, %, %, %, %); """

#print(songplay)

# FIND SONGS

song_select = (""" SELECT * FROM songs
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]