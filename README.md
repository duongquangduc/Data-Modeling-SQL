<h1>Project: Data Modeling with Postgres</h1>

<h2>1. Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.</h2>
<p>This database is about storing music and artist records. Data is extracted from the source, then transformed using Pandas DataFrame, and finally loaded into the database. 
There are two sets of data used in the ETL process: song and log data. Song data provides song and artist information, while log data is provides covers song, artist and some metadata of each song.</p>

<p>Source data stands into json files</p>

<h2>2. State and justify your database schema design and ETL pipeline.</h2>

<p>Fact Table:</p>
<p>songplays - records in log data associated with song plays i.e. records with page NextSong</p>
<p>songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent</p>

<p>Dimension Tables:</p>
<p>users - users in the app</p>
<p>user_id, first_name, last_name, gender, level</p>

<p>songs - songs in music database</p>
<p>song_id, title, artist_id, year, duration</p>

<p>artists - artists in music database</p>
<p>artist_id, name, location, lattitude, longitude</p>

<p>time - timestamps of records in songplays broken down into specific units</p>
<p>start_time, hour, day, week, month, year, weekday</p>

<h2>How to run the program</h2>
<p>Execute "create_tables.py". </p>
<p>Execute "etl.py". </p>

<h2>Introduction of the files</h2>
<p>test.ipynb displays the first rows of each table to check database.</p>
<p>create_tables.py drops and creates your tables.</p></p>
<p>etl.ipynb reads and processes a single file from song_data and log_data and loads the data into your tables. Thi
<p>etl.py reads and processes files from song_data and log_data and loads them into your tables.
<p>sql_queries.py contains all sql queries, and is imported into the last three files above.