# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = """ CREATE TABLE songplays 
(songplay_id serial, start_time timestamp, user_id text, level char, song_id text, artist_id text, session_id text, location text, user_agent text, 
PRIMARY KEY ( user_id, artist_id))"""

user_table_create = """ CREATE TABLE users 
(user_id text, first_name text, last_name text, gender char, level text, PRIMARY KEY ( user_id) )"""

song_table_create = """ CREATE TABLE songs 
(song_id text, title text, artist_id text, year int, duration int, PRIMARY KEY ( song_id, artist_id ) )"""

artist_table_create = """ CREATE TABLE artists 
(artist_id text, name text, location text, latitude numeric, longitude numeric, PRIMARY KEY ( artist_id ) )"""

time_table_create = """ CREATE TABLE time 
(start_time timestamp, hour int, day int, week int, month int, year int,  weekday int, PRIMARY KEY ( start_time ) )"""

# INSERT RECORDS

songplay_table_insert = """INSERT INTO songplays
(songplay_id, start_time, user_id, level, song_id, artist_id,  session_id, location, user_agent) VALUES( %, %, %, %, %, %, %, %, %);"""

user_table_insert = """INSERT INTO users
( user_id, first_name, last_name, gender, level) VALUES( %s, %s, %s, %s, %s) ON CONFLICT(user_id) DO NOTHING; """

song_table_insert = """INSERT INTO songs 
(song_id, title, artist_id, year, duration)  VALUES( %, %, %, %, %) ON CONFLICT(song_id, artist_id) DO NOTHING ; """

artist_table_insert = """INSERT INTO artists
(artist_id, name, location, latitude, longitude)  VALUES( %, %, %, %, %)ON CONFLICT(artist_id) DO NOTHING; """


time_table_insert = """INSERT INTO time 
(start_time, hour, day, week, month, year, weekday)  VALUES( %s, %s, %s, %s, %s, %s, %s) ON CONFLICT(start_time) DO NOTHING; """

#print(songplay)

# FIND SONGS

song_select = (""" SELECT song_id, artist_id FROM songs
""")

#ts, level, user_id, song_id, session_id, location, user_agent

#, user ID, level, song ID, artist ID, session ID, location, and user agent 

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]